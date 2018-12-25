import re


class CheckWord:
    def __init__(self):
        self.blacklist = set()
        self.whitelist = set()

    def __word_check(self, text, list_type='blacklist', match_case=False, words=True):
        reg = r'{}'
        list_obj = self.blacklist if list_type == 'blacklist' else self.whitelist
        if not match_case:
            text = text.lower()
        if words:
            reg = r'\b{}\b'
        for rule in list_obj:
            if not match_case:
                rule = rule.lower()
            result = re.search(reg.format(rule), text)
            if result:
                return True
        return False

    def __add_words(self, words, list_type='blacklist'):
        list_obj = self.blacklist
        if list_type == 'whitelist':
            list_obj = self.whitelist
        if not isinstance(words, (list, tuple)):
            words = [words, ]
        list_obj.update(words)

    def __remove_word(self, word, list_type='blacklist'):
        list_obj = self.blacklist
        if list_type == 'whitelist':
            list_obj = self.whitelist
        list_obj.remove(word)

    def blacklisted(self, text):
        self.__word_check(text)

    def whitelisted(self, text):
        self.__word_check(text, list_type='whitelist')

    def update_blacklist(self, obj):
        self.__add_words(obj)

    def update_whitelist(self, obj):
        self.__add_words(obj, 'whitelist')

    def remove_word_from(self, word, list_type):
        self.__remove_word(word, list_type)

    def clear_list(self, list_type):
        list_obj = self.blacklist
        if list_type == 'whitelist':
            list_obj = self.whitelist
        list_obj.clear()
