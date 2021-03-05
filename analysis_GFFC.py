import os



def user_id():

	p_user_id = open("./result_GFFC/id.db","r")
	user_id = p_user_id.read()
	p_user_id.close()

	return user_id



def count_all(user_id):

	count_all_pwd = "./result_GFFC/" + user_id + "-count.db"

	p_count_all = open(count_all_pwd,"r")
	count_all = p_count_all.read()
	p_count_all.close()

	count_all = count_all.split(",")

	count_followers = count_all[0]
	count_following = count_all[1]

	return int(count_followers), int(count_following)





def check_my_person(user_id, count_following, count_followers):


	check_followers_name = "./result_GFFC/" + user_id + "-followers.db"
	check_following_name = "./result_GFFC/" + user_id + "-following.db"

	p_followers_name = open(check_followers_name,"r")
	p_following_name = open(check_following_name,"r")


	following_array = []

	for i in range(0,count_following + 1):

		following_array.append(p_following_name.readline()[4:].replace("\n",""))

	p_following_name.close()

	del following_array[0]




	followers_array = []

	for i in range(0,count_followers + 1):

		followers_array.append(p_followers_name.readline()[4:].replace("\n",""))

	p_followers_name.close()

	del followers_array[0]



	following_person = 1
	page = 1
	result_print = "\n\n\n  [ " + str(page) + " ] Page | https://github.com/" + user_id + "?tab=following&page=" + str(page) + "\n"
	for following_name in following_array:

		if following_person == 51:

			following_person = 1
			page += 1
			result_print += "\n\n\n  [ " + str(page) + " ] Page | https://github.com/" + user_id + "?tab=following&page=" + str(page) + "\n"


		else:
			pass


		if following_name in followers_array:

			result_print += "    yes " + following_name + "\n"

		else:

			result_print += "    [ no ] " + following_name + "\n"


		following_person += 1



	result_print += "\n\n\n"

	os.system("rm -rf ./result_GFFC/" + user_id + "-result.db")
	os.system("touch ./result_GFFC/" + user_id + "-result.db")

	pwd = "./result_GFFC/" + user_id + "-result.db"
	f = open(pwd,"w")
	f.write(result_print)
	f.close()

	print "\n\n    [ Done ] Check the File -> ./result_GFFC/" + user_id + "-result.db\n\n"




if __name__ == "__main__":

	user_id = user_id()

	count_followers, count_following = count_all(user_id)

	result_print = check_my_person(user_id, count_following, count_followers)

