import sys
import logging

from . import rcp_checker

logging.basicConfig(filename='rcp_checker.log', encoding='utf-8', level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())
formatter = logging.Formatter("%(levelname)s - %(message)s")
logging.getLogger().handlers[0].setFormatter(formatter)

parser = rcp_checker.get_parser()
args = parser.parse_args()

# Results summarizer makes these 3 calls to invoke RCP test
checker = rcp_checker.make_checker(args.rcp_usage, args.rcp_version, args.verbose, args.bert_train_samples)
checker._compute_rcp_stats()
test, msg = checker._check_directory(args.dir)

if test:
    logging.info("%s ,RCP test passed", msg)
else:
    logging.info("%s ,RCP test failed", msg)
    sys.exit(1)
