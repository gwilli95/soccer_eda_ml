import pathlib

SOCCER_DATABASE = "hugomathien/soccer"
SOURCE_PATH = pathlib.Path.cwd().resolve().parent
DATA_PATH = SOURCE_PATH.joinpath("data")
NOTEBOOKS_PATH = SOURCE_PATH.joinpath("notebooks")
MODELS_PATH = SOURCE_PATH.joinpath("models")