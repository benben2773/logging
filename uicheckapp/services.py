import logging

logger = logging.getLogger(__name__)  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger

class EchoService:
  def echo(self, msg):
    print(f"Logger name = {logger.name} , is propagate = {logger.propagate} level = {logger.level}")
    print(f"logger parent = {logger.parent.name}")
    print(f"logger parent's parent = {logger.parent.parent.name}")
    
    logger.debug("echoing something from the uicheckapp logger")
    print(msg)
