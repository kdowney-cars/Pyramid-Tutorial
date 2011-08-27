from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramid_tutorial.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'test_jinja2')
    
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    
    #config = Configurator(root_factory=get_root, settings=settings)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'pyramid_tutorial:static')
    config.add_route('home', '/')
    config.add_view('pyramid_tutorial.views.my_view',
                    route_name='home',
                    renderer='templates/mytemplate.pt')
 
    #config.add_translation_dirs('locale/')
    config.include('pyramid_jinja2')
    
    return config.make_wsgi_app()

