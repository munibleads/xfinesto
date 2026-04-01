"""
LLM client wrapper
Unified OpenAI-format API calls
"""

import json
import re
import time
from typing import Optional, Dict, Any, List
from openai import OpenAI, RateLimitError

from ..config import Config


class LLMClient:
    """LLM client"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        self.api_key = api_key or Config.LLM_API_KEY
        self.base_url = base_url or Config.LLM_BASE_URL
        self.model = model or Config.LLM_MODEL_NAME

        if not self.api_key:
            raise ValueError("LLM_API_KEY is not configured")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """
        Send a chat request.

        Args:
            messages: List of messages
            temperature: Temperature parameter
            max_tokens: Maximum token count
            response_format: Response format (e.g. JSON mode)

        Returns:
            Model response text
        """
        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        if response_format:
            kwargs["response_format"] = response_format

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(**kwargs)
                content = response.choices[0].message.content
                # Some models (e.g. MiniMax M2.5) include <think> reasoning content in the response, which must be stripped
                content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
                return content
            except RateLimitError as e:
                if attempt < max_retries - 1:
                    wait = self._parse_retry_wait(str(e), fallback=30 * (attempt + 1))
                    # Cap at 5 minutes — beyond that the daily limit is exhausted; re-raise so caller knows
                    if wait > 300:
                        raise
                    time.sleep(wait)
                else:
                    raise

    @staticmethod
    def _parse_retry_wait(error_message: str, fallback: float = 30) -> float:
        """Parse the suggested wait time from a Groq 429 error message.

        Handles formats like '25.092s' and '14m53.088s'.
        Returns seconds as a float, or fallback if not parseable.
        """
        match = re.search(r'try again in ((?:\d+m)?\d+(?:\.\d+)?s)', error_message)
        if not match:
            return fallback
        raw = match.group(1)
        minutes = re.search(r'(\d+)m', raw)
        seconds = re.search(r'(\d+(?:\.\d+)?)s', raw)
        total = 0.0
        if minutes:
            total += int(minutes.group(1)) * 60
        if seconds:
            total += float(seconds.group(1))
        return total if total > 0 else fallback

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        Send a chat request and return JSON.

        Args:
            messages: List of messages
            temperature: Temperature parameter
            max_tokens: Maximum token count

        Returns:
            Parsed JSON object
        """
        response = self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        # Strip markdown code block markers
        cleaned_response = response.strip()
        cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
        cleaned_response = cleaned_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON returned by LLM: {cleaned_response}")
