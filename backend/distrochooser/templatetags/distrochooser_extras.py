from django import template
from distrochooser.constants import TRANSLATIONS
from distrochooser.models import Distribution, AnswerDistributionMatrix, Answer, UserSuggestion, UserSuggestionSession
register = template.Library()

@register.inclusion_tag('tag_distro.html')
def tag_distro(distro: Distribution, matrix_tuple: AnswerDistributionMatrix, answer: Answer, suggestion: UserSuggestion = None ):
    return {'distro': distro, 'matrix_tuple': matrix_tuple, 'answer': answer, 'suggestion': suggestion}


@register.inclusion_tag('tag_selection.html')
def tag_selection(matrix_tuple: AnswerDistributionMatrix, answer: Answer, language_code: str, session: UserSuggestionSession):
    return {'matrix_tuple': matrix_tuple, 'answer': answer, 'language_code': language_code, "session": session}

@register.simple_tag
def i(value: str, lang: str):
    # even as Django has it's own i18n system, the majority in this project was build for the frontend, not utilizing this. Which was kind of dumb.
    # To prevent using two systems for translating, this method will be used to parse the existing translations
    # This might change in later versions
    return TRANSLATIONS[lang][value] if value in TRANSLATIONS[lang] else value

@register.simple_tag
def has_suggestions(matrix: AnswerDistributionMatrix, session: UserSuggestionSession) -> bool:
    return matrix.has_suggestions(session)

@register.simple_tag
def delete_suggestion(matrix: AnswerDistributionMatrix, session: UserSuggestionSession) -> AnswerDistributionMatrix | None:
    return matrix.get_delete_suggestion(session)

@register.simple_tag
def distro_suggestions(matrix: AnswerDistributionMatrix, session: UserSuggestionSession):
    return matrix.get_distro_suggestions(session)

@register.simple_tag
def distro_removal_suggestions(matrix: AnswerDistributionMatrix, session: UserSuggestionSession):
    return matrix.get_distro_removal_suggestions(session)