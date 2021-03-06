from ast import literal_eval
import json
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


	# del First line
	p_followers_name.readline()
        p_following_name.readline()


	following_list = []
	following_list_v1 = ""

	# if i == 0   ->   ( 0 % 50 ) == 0  ->  range(1,count_following + 2 )
	for i in range(1,count_following + 2):

		try:

      		  	prepare_array_v1 = p_following_name.readline().split("] ")


			#print prepare_array_v1

			#following_list = prepare_array_v1

			#page = prepare_array_v1[0].replace("[","")

			following_id = prepare_array_v1[1].replace("\n","")

			following_list_v1 += following_id + ","

			if ( i % 50 ) == 0:

				following_list_v2 = following_list_v1[:-1].split(",")

				following_list.append(following_list_v2)

				following_list_v1 = ""

				#print page

	        except IndexError:

			#following_list.append(following_id)
			pass



	p_following_name.close()


	#print following_list







	#print s

	#print following_list

	#del following_array[0]

	#following_dic = following_dic[0] + following_dic[42:-1] + '}'

	#following_dic = json.loads(following_dic)

	#print following_dic

	#print type(following_dic)

	#print following_dic




	followers_list = []
	followers_list_v1 = ""

	for i in range(1,count_followers + 2):

		try:

      		  	prepare_array_v1 = p_followers_name.readline().split("] ")

			#print prepare_array_v1

			#followers_list = prepare_array_v1

			page = prepare_array_v1[0].replace("[","")

			followers_id = prepare_array_v1[1].replace("\n","")

			followers_list_v1 += followers_id + ","

			if ( i % 50 ) == 0:

				followers_list_v2 = followers_list_v1[:-1].split(",")

				followers_list.append(followers_list_v2)

				followers_list_v1 = ""

				#print page

	        except IndexError:

			#followers_list.append(followers_id)
			pass



	p_followers_name.close()

	#print followers_list








	result_print = ""

	#for i in (1, count_following +2 ):

	for i in range(0, len(following_list)):

		for j in range(0, len(following_list[i])):

			print following_list[i][j]
			print i

			if following_list[i][j] in followers_list[i]:

				pass
				#print "Yes " + following_list[i][j] + "\n"

			else:
				pass
				#print "No " + following_list[i][j] + "\n"



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

