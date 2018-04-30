from sanic import Sanic
from sanic_graphql import GraphQLView
from lib.graphql.schema import schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from sanic_cors import CORS
# import pdb; pdb.set_trace()

app = Sanic(__name__)
app.debug = True
CORS(app, automatic_options=True)

class GraphQL(GraphQLView):
  def get_root_value(self, request):
    return request

@app.listener('before_server_start')
def init_async_executor(app, loop):
    executor = AsyncioExecutor(loop)
    app.add_route(GraphQL.as_view(schema=schema, graphiql=True, executor=executor), '/graphql')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=app.config.PORT)