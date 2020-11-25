from core.testingKit_app.puppeteer import Puppeteer

from demos.testing_app.solution_parameter import *
from demos.testing_app.modes.mode_system import ModeSystem


puppeteer = Puppeteer.get_driver(SOLUTION_DRIVER_CONFIG_PATH)

mode = ModeSystem(puppeteer)

mode.home_upward_arrows.tap()

