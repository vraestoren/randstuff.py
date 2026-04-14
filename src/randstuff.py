from requests import Session

class RandStuff:
	def __init__(self) -> None:
		self.api = "https://randstuff.ru"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
			"X-Requested-With": "XMLHttpRequest"
		}

	def _post(self, endpoint: str, data: dict = None) -> dict:
		return self.session.post(
			f"{self.api}{endpoint}", data=data).json()

	def generate_random_joke(self) -> dict:
		return self._post("/joke/generate")

	def generate_random_number(
			self,
			count: int = 1,
			start: int = 1,
			end: int = 100,
			numbers_list: str = None,
			unique: int = 0,
			timezone: int = -480) -> dict:
		data = {
			"count": count,
			"from": "range",
			"start": start,
			"end": end,
			"list": numbers_list,
			"unique": unique,
			"tz": timezone
		}
		return self._post(
			"/number/generate/", data)

	def generate_random_wisdom(self) -> dict:
		return self._post("/saying/generate/")

	def generate_random_fact(self) -> dict:
		return self._post("/fact/generate/")

	def generate_random_ticket(self) -> dict:
		return self._post("/ticket/generate/")

	def get_random_ask(self, question: str) -> dict:
		data = {
			"question": question
		}
		return self._post("/ask/generate/", data)

	def generate_random_password(
			self,
			length: int = 8,
			numbers: int = 0,
			symbols: int = 0) -> dict:
		data = {
			"length": length,
			"numbers": numbers,
			"symbols": symbols
		}
		return self._post("/password/generate/", data)

	def generate_random_question(self) -> dict:
		return self._post("/question/generate/")

	def answer_to_question(
			self,
			question_id: int,
			number: int) -> dict:
		data = {
			"id": question_id,
			"number": number
		}
		return self._post("/question/answer/", data)

	def generate_random_nickname(
			self,
			numbers: int = 1) -> dict:
		data = {
			"numbers": numbers
		}
		return self._post("/nickname/generate/", data)

	def generate_random_city(self, country: str = "all") -> dict:
		data = {
			"country": country
		}
		return self._post("/city/generate/", data)
