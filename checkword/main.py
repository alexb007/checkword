from .processor import Processor

whitelist = Processor()
blacklist = Processor()


def blacklisted(text, match_case=False, words=True):
    """
    Check if text contains blacklisted words
    :param text:
    :param match_case:
    :param words:
    :return:
    """
    return blacklist.check_text(text, match_case=match_case, words=words)


def whitelisted(text, match_case=False, words=True):
    """
    Check if text contains whitelisted words
    :param text:
    :param match_case:
    :param words:
    :return:
    """
    return whitelist.check_text(text, match_case=match_case, words=words)


def add_words(list_type, words):
    """
    Add words to list. `list_type` must be one of blacklist and whitelist
    :param list_type:
    :param words:
    :return:
    """
    list_obj = blacklist
    if list_type == 'whitelist':
        list_obj = whitelist
    elif list_type != 'blacklist':
        raise Exception("list_type expected blacklist or whitelist, but {} found".format(list_type))
    list_obj.update_container(words)


def remove_word(list_type, word):
    """
    Remove word from list. `list_type` must be one of blacklist and whitelist
    :param list_type:
    :param word:
    :return:
    """
    list_obj = blacklist
    if list_type == 'whitelist':
        list_obj = whitelist
    elif list_type != 'blacklist':
        raise Exception("list_type expected blacklist or whitelist, but {} found".format(list_type))
    list_obj.remove(word)


def clear(list_type, word):
    """
    Clear list. `list_type` must be one of blacklist and whitelist
    :param list_type:
    :param word:
    :return:
    """
    list_obj = blacklist
    if list_type == 'whitelist':
        list_obj = whitelist
    elif list_type != 'blacklist':
        raise Exception("list_type expected blacklist or whitelist, but {} found".format(list_type))
    list_obj.clear()
