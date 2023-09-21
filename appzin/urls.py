from rest_framework import routers
from .views import *

routerAppzin = routers.DefaultRouter()

routerAppzin.register(r'alunos', AlunosViews)
routerAppzin.register(r'professores', ProfessoresViews)
routerAppzin.register(r'disciplinas', DisciplinasViews)
routerAppzin.register(r'disciplinasalunos', DisciplinaAlunoViews)
routerAppzin.register(r'planoaula', PlanoAulaViews)
routerAppzin.register(r'atividades', AtividadesViews)
routerAppzin.register(r'atividadealunos', AtividadeAlunoViews)
routerAppzin.register(r'frequencia', FrequenciaViews)
routerAppzin.register(r'frequenciaalunos', FrequenciaAlunoViews)
