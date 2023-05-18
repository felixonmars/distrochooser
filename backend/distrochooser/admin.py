from django.contrib import admin
from .models import Question, Answer, GivenAnswer, UserSession, ResultDistroSelection, Distribution, SelectionReason, Category, AnswerDistributionMatrix, UserSuggestion, UserSuggestionSession, AnswerTag, AnswerBaseTag

[admin.site.register(*models) for models in [
  (Question,),
]]

class DistributionAdmin(admin.ModelAdmin):
  list_display = ("name","identifier", "data_id", "ratings", "positive_ratings", "percentage", "rank", "clicks", )
admin.site.register(Distribution, DistributionAdmin)

class GivenAnswerAdmin(admin.ModelAdmin):
  list_display = ("session", "answer", "isImportant", "isLessImportant")
admin.site.register(GivenAnswer, GivenAnswerAdmin)

class ResultDistroSelectionAdmin(admin.ModelAdmin):
  list_display = ("distro", "session", "isApprovedByUser", "isDisApprovedByUser", )
admin.site.register(ResultDistroSelection, ResultDistroSelectionAdmin)

class UserSessionAdmin(admin.ModelAdmin):
  list_display = ("dateTime","calculationTime",  "sessionToken", "referrer", "remarks", "remarksProcessed", "language", "commit", "userAgent", )
admin.site.register(UserSession, UserSessionAdmin)

class SelectionReasonAdmin(admin.ModelAdmin):
  list_display = ("description", "isPositiveHit", "isBlockingHit", "isNeutralHit", "isImportant", "isRelatedBlocked", "isLessImportant",)
admin.site.register(SelectionReason, SelectionReasonAdmin)

class CategoryAdmin(admin.ModelAdmin):
  def get_ordering(self, request):
     return ['index']
admin.site.register(Category, CategoryAdmin)

class AnswerAdmin(admin.ModelAdmin):
  def get_ordering(self, request):
     return ['question']
admin.site.register(Answer, AnswerAdmin)

class AnswerDistributionMatrixAdmin(admin.ModelAdmin):
  list_display = ("answer", "description", "isSuggestion", "isBlockingHit", "isNegativeHit", "isNeutralHit", "isTagOnlyHit", "isNegativeSuggestion", "distro_list")
  def get_ordering(self, request):
     return ['answer__question']
admin.site.register(AnswerDistributionMatrix, AnswerDistributionMatrixAdmin)


class UserSuggestionAdmin(admin.ModelAdmin):
  list_display = ("distro","old_mapping", "new_mapping", "is_removal")
admin.site.register(UserSuggestion, UserSuggestionAdmin)

class UsesSuggestionSessionAdmin(admin.ModelAdmin):
  list_display = ("sessionToken", "readonlyToken",)
admin.site.register(UserSuggestionSession, UsesSuggestionSessionAdmin)

class AnswerTagAdmin(admin.ModelAdmin):
  pass
admin.site.register(AnswerTag, AnswerTagAdmin)
class AnswerBaseTagAdmin(admin.ModelAdmin):
  pass
admin.site.register(AnswerBaseTag, AnswerBaseTagAdmin)