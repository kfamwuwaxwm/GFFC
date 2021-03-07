# -*- coding: utf-8 -*-
import requests
import os
import time

global base_url
global tag_followers
global tag_following
global header
global logo
global span_v1
global span_v2


base_url = 'https://github.com/'
tag_followers = "?tab=followers&page="
tag_following = "?tab=following&page="
headers = {"User-Agent": "GFFL/2.2.3"}
span_v1 = '''<span class="Link--secondary">'''
span_v2 = '''<span class="Link--secondary pl-1">'''
logo = '''

     ██████╗ ███████╗███████╗ ██████╗
    ██╔════╝ ██╔════╝██╔════╝██╔════╝
    ██║  ███╗█████╗  █████╗  ██║
    ██║   ██║██╔══╝  ██╔══╝  ██║
    ╚██████╔╝██║     ██║     ╚██████╗
     ╚═════╝ ╚═╝     ╚═╝      ╚═════╝

  ## Github Followers Following Check ##'''


def cc():

	os.system("clear && printf '\033[3J'")


def prepare_http(user_id):

	result_followers = "[Page] " + user_id + " followers\n"
	result_following = "[Page] " + user_id + " following\n"
	follower_url = "https://api.github.com/users/" + user_id

	response = requests.get(follower_url, headers=headers )

	rsp = response.text
	rsp_followers = rsp.split('''"followers":''')[1]
	rsp_followers = rsp_followers.split(",")[0]

	rsp_following = rsp.split('''"following":''')[1]
	rsp_following = rsp_following.split(",")[0]

	return result_followers, result_following, rsp_followers, rsp_following



def dashboard(user_id, rsp_followers, rsp_following):

	dash = logo + "\n\n\n"
	dash += "  Input Github User ID  > " + user_id + "\n\n\n"

	dash += "  ## Information ##\n"
	dash += "  [+] followers : " + str(rsp_followers) + "\n"
	dash += "  [+] following : " + str(rsp_following) + "\n"

	return dash


def followers(user_id, result_followers, rsp_followers, dash):

	followers_cnt = int(rsp_followers)
	pre_cnt = ( followers_cnt / 50 ) + 2
	cnt_print = pre_cnt - 1

	for cnt in range(1,pre_cnt):

		cc()

		print dash

		followers_pg = "\n  ## followers Progress ##"
		followers_pg += "\n  [+] " + str(cnt) + " / " + str(cnt_print) + " [ Max: " + str(cnt_print) + " ]"

		print followers_pg

		url = base_url + user_id + tag_followers + str(cnt)
		response = requests.get(url , headers=headers )

		# If you don't sleep, it's a DOS attack on the GitHub.
		time.sleep(1)

		rsp = response.text
		rsp_1 = rsp.split(span_v1)
		f = len(rsp_1)
		f = int(f)

		for i in range(1,f):

			followers = rsp_1[i].split("</span>")[0]
			result_followers += "[" + str(cnt) + "] " + followers + "\n"


		rsp_2 = rsp.split(span_v2)
		f = len(rsp_2)
		f = int(f)

		for i in range(1,f):

			followers = rsp_2[i].split("</span>")[0]
			result_followers += "[" + str(cnt) + "] " + followers + "\n"

	print "\n\n"
	return result_followers, followers_pg



def following(user_id, result_following, rsp_following, followers_pg, dash):

	following_cnt = int(rsp_following)
	pre_cnt = ( following_cnt / 50 ) + 2
	cnt_print = pre_cnt - 1

	for cnt in range(1,pre_cnt):

		cc()

		print dash
		print followers_pg

		print "\n\n  ## following Progress ##"
		print "  [+] " + str(cnt) + " / " + str(cnt_print) + " [ Max: " + str(cnt_print) + " ]"

		url = base_url + user_id + tag_following + str(cnt)
		response = requests.get(url , headers=headers )

		# If you don't sleep, it's a DOS attack on the GitHub.
		time.sleep(1)

		rsp = response.text
		rsp_1 = rsp.split(span_v1)
		f = len(rsp_1)
		f = int(f)

		for i in range(1,f):

			folloing = rsp_1[i].split("</span>")[0]
			result_following += "[" + str(cnt) + "] " + folloing + "\n"


		rsp_2 = rsp.split(span_v2)
		f = len(rsp_2)
		f = int(f)

		for i in range(1,f):

			following = rsp_2[i].split("</span>")[0]
			result_following += "[" + str(cnt) + "] " + following + "\n"



	print "\n"
	return result_following


def file_save(user_id, result_followers, result_following, rsp_followers, rsp_following):


	os.system("rm -rf ./result_GFFC")
	os.system("mkdir ./result_GFFC")

	id = "./result_GFFC/id.db"
	all = "./result_GFFC/" + user_id + "-all.db"
	count = "./result_GFFC/" + user_id + "-count.db"
	followers = "./result_GFFC/" + user_id + "-followers.db"
	following = "./result_GFFC/" + user_id + "-following.db"


	os.system("touch " + followers + " " + following + " " + all + " " + count + " " + id)


	file_id_db = "./result_GFFC/id.db"
	file_id_t = open(file_id_db,"w")
	file_id_t.write(user_id)
	file_id_t.close()

	file_ff_db = "./result_GFFC/" + user_id + "-count.db"
	file_ff_t = open(file_ff_db,"w")
	file_ff_t.write(rsp_followers + "," + rsp_following)
	file_ff_t.close()

	file_followers_db = "./result_GFFC/" + user_id + "-followers.db"
	file_followers_t = open(file_followers_db,"w")
	file_followers_t.write(result_followers)
	file_followers_t.close()

	file_following_db = "./result_GFFC/" + user_id + "-following.db"
	file_following_t = open(file_following_db,"w")
	file_following_t.write(result_following)
	file_following_t.close()

	file_all_db = "./result_GFFC/" + user_id + "-all.db"
	file_all_t = open(file_all_db,"w")
	file_all_t.write(result_followers + "\n\n" +result_following)
	file_all_t.close()

	print "  ## result file ##"
	print "  [+] id                    > ./result_GFFC/id.db"
	print "  [+] count                 > ./result_GFFC/" + user_id + "-count.db"
	print "  [+] followers             > ./result_GFFC/" + user_id + "-followers.db"
	print "  [+] following             > ./result_GFFC/" + user_id + "-following.db"
	print "  [+] followers + following > ./result_GFFC/" + user_id + "-all.db"

	print "\n\n  ## How to Check ##"
	print "  [+] python analysis_GFFC.py\n\n"


if __name__ == "__main__":

	cc()

	print logo + "\n\n"

	user_id = raw_input("  Input Github User ID  > ")

	result_followers, result_following, rsp_followers, rsp_following = prepare_http(user_id)

	dash = dashboard(user_id, rsp_followers, rsp_following)

	result_followers, followers_pg = followers(user_id, result_followers, rsp_followers, dash)

	result_following = following(user_id, result_following, rsp_following, followers_pg, dash)

	file_save(user_id, result_followers, result_following, rsp_followers, rsp_following)

