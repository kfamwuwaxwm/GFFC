from ast import literal_eval
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



	following_dic = '{'

	for i in range(0,count_following + 1):


		try:

                        prepare_array_v1 = p_following_name.readline().split("] ")

			page = prepare_array_v1[0].replace("[","")

			following_id = prepare_array_v1[1].replace("\n","")

			#following_dic = {page:following_id}

			following_dic += "'" + page
			following_dic += "':'" + following_id
			following_dic += "',"

		# count_following != real count_following
                except IndexError:

                        pass

	p_following_name.close()

	#del following_array[0]

	following_dic = following_dic[0] + following_dic[43:-1] + '}'

	following_dic = literal_eval(following_dic)

	print following_dic

	print type(following_dic)

	#print following_dic






	followers_array = []

	for i in range(0,count_followers + 1):


		try:

                        prepare_array_v1 = p_followers_name.readline().split("] ")

			followers_id = prepare_array_v1[1].replace("\n","")

			followers_array.append(followers_id)

		# count_followers != real count_followers
                except IndexError:

                        pass

	p_followers_name.close()

	del followers_array[0]


	#print followers_array




	result_print = ""

	for page, following_id  in following_dic.items():

		if following_id in followers_array:

			result_print += "    | yes |||||||| Page = " + str(page) + " | " + following_id + "\n"

		else:

			result_print += "    | $$ no $$ ||| Page = " + str(page) + " | " + following_id + "\n"

		#print page , following_id + "\n"

	#print result_print



	'''
	result_print += "\n\n\n"

	os.system("rm -rf ./result_GFFC/" + user_id + "-result.db")
	os.system("touch ./result_GFFC/" + user_id + "-result.db")

	pwd = "./result_GFFC/" + user_id + "-result.db"
	f = open(pwd,"w")
	f.write(result_print)
	f.close()

	print "\n\n    [ Done ] Check the File -> ./result_GFFC/" + user_id + "-result.db\n\n"
	'''



if __name__ == "__main__":

	user_id = user_id()

	count_followers, count_following = count_all(user_id)

	result_print = check_my_person(user_id, count_following, count_followers)

