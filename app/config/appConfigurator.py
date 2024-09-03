# config/appConfigurator.py

import logging

from ..security import SecurityConfig, SecurityHandlers
from ..exceptions import ApiHandlerException

from app.domain.gest_pessoas.cidade import CidadeCache
from app.domain.gest_pessoas.sexo import SexoCache
from app.domain.gest_usuarios.role import RoleCache


class AppConfigurator:
    """Classe para configurar o aplicativo Flask durante a inicialização."""

    def __init__(self, app):
        self.app = app
        logging.info("0: AppConfigurator.__init__()")

    def configure(self):
        with self.app.app_context():
            # Configurações e manipuladores
            SecurityConfig(self.app)
            SecurityHandlers(self.app)
            ApiHandlerException(self.app)

            CidadeCache().initialize_cidade_cache()
            SexoCache().initialize_sexo_cache()
            RoleCache().initialize_role_cache()

            logging.info("1: AppConfigurator.configure: CidadeCache: %s",
                         CidadeCache.get_cidade_cache())
            logging.info("2: AppConfigurator.configure: SexoCache: %s",
                         SexoCache.get_sexo_cache())
            logging.info("3: AppConfigurator.configure: RoleCache: %s",
                         RoleCache.get_role_cache())
