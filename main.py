# Brodderick Rodriguez
# Auburn University - CSSE
# July 12 2019

import logging
import sys
from xcsr.xcsr_driver import XCSRDriver
from xcsr.xcsr import XCSR
from xcsr import util


def human_play_rmux():
    from xcsr.example_scenarios.rmux.rmux_env import RMUXEnvironment
    from xcsr.example_scenarios.rmux.rmux_rp import RMUXReinforcementProgram

    rp = RMUXReinforcementProgram()
    env = RMUXEnvironment()
    env.human_play(reinforcement_program=rp)


def rmux():
    from xcsr.example_scenarios.rmux.rmux_env import RMUXEnvironment
    from xcsr.example_scenarios.rmux.rmux_rp import RMUXReinforcementProgram
    from xcsr.example_scenarios.rmux.rmux_config import RMUXConfiguration

    driver = XCSRDriver()
    driver.repetitions = 5
    driver.save_location = './xcsr/example_scenarios/rmux/data'
    driver.experiment_name = 'test16'

    driver.xcs_class = XCSR
    driver.environment_class = RMUXEnvironment
    driver.reinforcement_program_class = RMUXReinforcementProgram
    driver.configuration_class = RMUXConfiguration

    driver.run()

    dir_name = './xcsr/example_scenarios/rmux/data/' + driver.experiment_name
    util.plot_results(dir_name, title='RMUX', interval=50)


if __name__ == '__main__':
    print('XCS')
    # logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # human_play_rmux()
    rmux()


