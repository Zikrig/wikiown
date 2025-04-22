import httpx
from typing import Dict, Optional
from openai import OpenAI
import json
import re

from config import DEEPSEEK_TOKEN, DEEPSEEK_URL

class Deepseek:
    def __init__(self):
        self.api_key = DEEPSEEK_TOKEN
        self.api_url = DEEPSEEK_URL
        self.client = OpenAI(api_key=self.api_key, base_url=self.api_url)


    def generate_text(
        self,
        prompt: str,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        top_p: float = 0.9,
        stop: Optional[list] = None,
        # model="deepseek-chat",
        model="deepseek-reasoner"
    ) -> Dict:
        """
        Генерирует текст с помощью Deepseek API
        
        Args:
            prompt: текст запроса
            max_tokens: максимальное количество токенов в ответе
            temperature: температура генерации (0.0 - 1.0)
            top_p: параметр top_p для генерации
            stop: список стоп-слов
            
        Returns:
            Dict: ответ от API
        """
        try:
            messages = [{"role": "user", "content": prompt}]
            
            completion = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                stop=stop,
                stream=False
            )
            
            response = completion.choices[0].message
            return {
                "status": "success",
                "data": response.content
            }
        
        except httpx.HTTPError as e:
            return {
                "status": "error",
                "message": f"HTTP error: {str(e)}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error: {str(e)}"
            } 