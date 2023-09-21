from rest_framework import routers
from .views import *

routerAppzin = routers.DefaultRouter()

routerAppzin.register(r'user', UserViews)
routerAppzin.register(r'contas', ContasViews)
routerAppzin.register(r'ufs', UfsViews)
routerAppzin.register(r'cidades', CidadesViews)
routerAppzin.register(r'enderecos', EnderecosViews)
routerAppzin.register(r'pessoas', PessoasViews)
routerAppzin.register(r'ocorrencias', OcorrenciasViews)
