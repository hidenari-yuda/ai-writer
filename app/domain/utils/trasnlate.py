import config.config
import deepl


class Translate:

    def __init__(self):
        pass

    def translate_to_japanese(self, text) -> str:
        source_lang = 'EN'
        target_lang = 'JA'

        # Initialize the translator
        api_key = config.config.DEEPL_API_KEY
        print('api_key is', api_key)
        translator = deepl.Translator(api_key)

        # Execute the translation
        result = translator.translate_text(
            text, source_lang=source_lang, target_lang=target_lang)

        # result
        print('resut is', result)

        return result.text

    def translate_list_to_japanese(self, text_list) -> list:
        source_lang = 'EN'
        target_lang = 'JA'

        # Initialize the translator
        translator = deepl.Translator(config.config.DEEPL_API_KEY)

        # Execute the translation
        results = translator.translate_text(
            text_list, source_lang=source_lang, target_lang=target_lang)

        # result
        for result in results:
            print(result)
            # 翻訳後の文章にアクセスする場合は .text で可能
            # print(result.text)

        return results
