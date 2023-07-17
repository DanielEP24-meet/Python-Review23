def create_youtube_video(title : str , description : str , hashtags : list) -> dict:
	vid = {
		"title" : title,
		"description" : description,
		"like" : 0,
		"dislike" : 0,
		"comments" : 
		{

			
		},
		"hashtags" : hashtags
	}
	return vid


def like(yt_vid : dict) -> dict:
	if "like" in yt_vid:
		yt_vid["like"] += 1
		return yt_vid
	else:
		yt_vid["like"] = 1
		return yt_vid



def dislike(yt_vid : dict) -> dict:
	if "like" in yt_vid:
		yt_vid["dislike"] += 1
		return yt_vid
	else:
		yt_vid["dislike"] = 1
		return yt_vid


def add_comment(yt_vid : dict , username : str , comment_content : str) -> dict:
	yt_vid["comments"][username] = comment_content
	return yt_vid 


def check_precentage_of_hashtags(yt_vid1 : list , yt_vid2 : list) -> float:
	maxarray = max(len(yt_vid1) , len(yt_vid2))
	common = (set(yt_vid1) & set(yt_vid2))
	if common:
		return (len(common) / maxarray) * 100
	else:
		return 0





#In order to add 495 likes I would use Either Recursion or a for loop, since we are using python I chose the for loop
video = create_youtube_video("A video with 495 likes" , "one day this video wil have 495 likes!!!" , ["#amazingvid" , "#inlove"])
video1 = create_youtube_video("A video " , "I Have the same hashtags as the video above me(or do I?)" , ["#amazingvid" , "#inlove" , "#fyp"])
for i in range(0,495):
	video = like(video)

print(video)
print(check_precentage_of_hashtags(video["hashtags"] , video1["hashtags"]))


