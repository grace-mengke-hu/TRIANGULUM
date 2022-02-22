#userInfo is a list of dictionary, i is the post location after sorting according to time
#{'genLabel': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], '1492748134': '/uufs/chpc.utah.edu/common/home/conway-group1/TRIANGULUM_ANNOTATION/AnnotationDataset/userBasedData/4-10/Corpus/10_Krispyy_Kris_1492748134_66n0e5_trees.txt', 'corpus': 'Sesh Hounds preparing to wrap our first 12 inch joint. Happy 4/20 frents\n\n', 'subreddit': 'trees'}
def convert(listInt):
	out = []
	for i in listInt:
		out.append(str(i))
	return ''.join(out)

def post2features(userInfo, i):
	post = userInfo[i]['corpus']
	label = convert(userInfo[i]['genLabel']) #'_'.join(userInfo[i]['genLabel'])
	subreddit = userInfo[i]['subreddit']
	features = [
		'bias',
		'doc.lower='+post.lower(),
		'tag='+label,
		'subreddit='+subreddit,
		'length='+str(len(post.split(' '))),
	]

	if i >0:
		post1 = userInfo[i-1]['corpus']
		label1 = convert(userInfo[i]['genLabel']) #'_'.join(userInfo[i-1]['genLabel'])
		subreddit1 = userInfo[i-1]['subreddit']
		features.extend([
			'-1:doc.lower='+post1.lower(),
			'-1:tag='+label1,
			'-1:subreddit='+subreddit1,
			'-1:length='+str( len(post1.split(' '))),
		])
	else:
		features.append('BOS')

	if i< len(userInfo)-1:
		post_1 = userInfo[i+1]['corpus']
		label_1 = convert(userInfo[i]['genLabel']) #'_'.join(userInfo[i+1]['genLabel'])
		subreddit_1 = userInfo[i+1]['subreddit']
		features.extend([
			'+1:doc.lower='+post_1.lower(),
			'+1:tag='+label_1,
			'+1:subreddit='+subreddit_1,
			'+1:length='+str(len(post_1.split(' '))),
		])
	else:
		features.append('EOS')

	return features

def userList2features(userInfo):
	return [post2features(userInfo, i) for i in range(len(userInfo))]

def userList2labels(userInfo):
	out = []
	outString = []
	for user in userInfo:
		for i in user['genLabel']:
			out.append(str(i))
		outString.append(''.join(out))
	return outString

	
