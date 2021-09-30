import sys
import logging

from . import mlp_compliance

logging.basicConfig(filename='compliance_checker.log', encoding='utf-8', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())
formatter = logging.Formatter("%(levelname)s - %(message)s")
logging.getLogger().handlers[0].setFormatter(formatter)

parser = mlp_compliance.get_parser()
args = parser.parse_args()

config_file = args.config or f'{args.usage}_{args.ruleset}/common.yaml'

checker = mlp_compliance.make_checker(
    args.usage,
    args.ruleset,
    args.quiet,
    args.werror,
)

valid, system_id, benchmark, result = mlp_compliance.main(args.filename, config_file, checker)

if not valid:
    logging.info('FAILED')
    sys.exit(1)
else:
    logging.info('SUCCESS')
