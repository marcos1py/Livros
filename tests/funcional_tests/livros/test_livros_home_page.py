from selenium.webdriver.common.by import By
import pytest

from .base import LivroBaseFunctionalTest

@pytest.mark.functional_test
class livroHomePageFunctionalTest(LivroBaseFunctionalTest):
    def test_livro_home_page_without_livros_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Nenhum livro encontrado aqui 🥲', body.text)