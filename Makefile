datasets/enwiki.observations.damaging.with_cache.20k_2015.json: \
		datasets/enwiki.observations.damaging.20k_2015.json
	cat datasets/enwiki.observations.damaging.20k_2015.json | \
	revscoring extract \
		editquality.feature_lists.enwiki.damaging \
		vector_demo.important_hash_delta.dependencies \
		--host https://en.wikipedia.org \
		--verbose > \
	datasets/enwiki.observations.damaging.with_cache.20k_2015.json

datasources/enwiki.damaging.important_hash_delta.datasource: \
		datasets/enwiki.observations.damaging.with_cache.20k_2015.json
	cat datasets/enwiki.observations.damaging.with_cache.20k_2015.json | \
	revscoring fit \
		vector_demo.important_hash_delta \
		damaging > \
	datasources/enwiki.damaging.important_hash_delta.datasource
