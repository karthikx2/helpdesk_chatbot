#  import logging
#  import json
#  from sanic import Blueprint, response
#  from sanic.request import Request
#  from typing import Text, Optional, List, Dict, Any

#  from rasa.core.channels.channel import UserMessage, OutputChannel
#  from rasa.core.channels.channel import InputChannel
#  from rasa.core.channels.channel import CollectingOutputChannel
#  import requests

#   from .custom_server import parse

#  import asyncio
#  import concurrent.futures
#  import logging
#  import multiprocessing
#  import os
#  import traceback
#  from collections import defaultdict
#  from functools import reduce, wraps
#  from inspect import isawaitable
#  from pathlib import Path
#  from http import HTTPStatus
#  from typing import (
#      Any,
#      Callable,
#      DefaultDict,
#      List,
#      Optional,
#      Text,
#      Union,
#      Dict,
#      TYPE_CHECKING,
#      NoReturn,
#      Coroutine,
#  )

#  import aiohttp
#  import jsonschema
#  from sanic import Sanic, response
#  from sanic.request import Request
#  from sanic.response import HTTPResponse
#  from sanic_cors import CORS
#  from sanic_jwt import Initialize, exceptions

#  import rasa
#  import rasa.core.utils
#  from rasa.nlu.emulators.emulator import Emulator
#  import rasa.utils.common
#  import rasa.shared.utils.common
#  import rasa.shared.utils.io
#  import rasa.shared.utils.validation
#  import rasa.shared.nlu.training_data.schemas.data_schema
#  import rasa.utils.endpoints
#  import rasa.utils.io
#  from rasa.shared.core.training_data.story_writer.yaml_story_writer import (
#      YAMLStoryWriter,
#  )
#  from rasa.shared.importers.importer import TrainingDataImporter
#  from rasa.shared.nlu.training_data.formats import RasaYAMLReader
#  from rasa.core.constants import DEFAULT_RESPONSE_TIMEOUT
#  from rasa.constants import MINIMUM_COMPATIBLE_VERSION
#  from rasa.shared.constants import (
#      DOCS_URL_TRAINING_DATA,
#      DOCS_BASE_URL,
#      DEFAULT_SENDER_ID,
#      DEFAULT_MODELS_PATH,
#      TEST_STORIES_FILE_PREFIX,
#  )
#  from rasa.shared.core.domain import InvalidDomain, Domain
#  from rasa.core.agent import Agent
#  from rasa.core.channels.channel import (
#      CollectingOutputChannel,
#      OutputChannel,
#      UserMessage,
#  )
#  import rasa.shared.core.events
#  from rasa.shared.core.events import Event
#  from rasa.core.test import test
#  from rasa.utils.common import TempDirectoryPath, get_temp_dir_name
#  from rasa.shared.core.trackers import (
#      DialogueStateTracker,
#      EventVerbosity,
#  )
#  from rasa.core.utils import AvailableEndpoints
#  from rasa.nlu.emulators.no_emulator import NoEmulator
#  import rasa.nlu.test
#  from rasa.nlu.test import CVEvaluationResult
#  from rasa.shared.utils.schemas.events import EVENTS_SCHEMA
#  from rasa.utils.endpoints import EndpointConfig

#  if TYPE_CHECKING:
#      from ssl import SSLContext
#      from rasa.core.processor import MessageProcessor
#      from mypy_extensions import Arg, VarArg, KwArg

 

#  logger = logging.getLogger(__name__)



#  class Custom_Channel_Response(InputChannel):

#      @classmethod
#      def name(cls):
#          print('Inside receive endpoint name')
#          return "custom_channel_response"

#      def _extract_message(self, req: Request) -> Optional[Text]:
#              return req.json.get("text", None)

#      def blueprint(self, on_new_message):

#          print('Inside receive endpoint blueprint')
        
#          custom_response_webhook = Blueprint("custom_response_webhook", __name__)

#          @custom_response_webhook.route("/", methods=["GET"])
#          async def health(request):
#              return response.json({"status": "ok"})


#          @custom_response_webhook.route("/webhook", methods=["POST"])
#          async def receive(request):


#              print('Inside receive endpoint receive')

#              text = self._extract_message(request)


#              payload = request.json

#              out = CollectingOutputChannel()

#              await on_new_message(UserMessage(text, out))

#              print(f"Message : {out.messages}")


#              responses = [m["text"] for m in out.messages]
#              message = responses[0]
#              session = "false"
            
#              intent =  parse_intent(request)
#             #  intent = requests.post(url = "http://3.145.51.33:5005/model/parse", json = payload, headers={'Content-Type': 'application/json'}) 
#              print(f"Intent : {intent}")


#              r = {
                 
#                   "response": {
#                      "outputSpeech": {
#                          "text": message,
#                          "intent": intent
#                      }
#                  }

#              }

#              return response.json(r)

#          return custom_response_webhook


