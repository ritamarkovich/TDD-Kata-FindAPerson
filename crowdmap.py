__author__ = 'olesya'


class Crowdmap():
    def __init__(self, l_post):
        self.posts_list = l_post

    def get_all_posts_for(self, name):
        list_of_posts = list()
        for l in self.posts_list:
            if name in l:
                list_of_posts.append(l)
        return list_of_posts

    def is_location(self, name):
        list_of_posts = self.get_all_posts_for(name)
        flag = False
        for l in list_of_posts:
            if "Bangkok" in l:
                flag = True
        return flag

    def is_location_for_post(self, post, location):
        flag = False
        if location in post:
            flag = True
        return flag

    def is_inconsistencies(self, name):
        list_of_posts = self.get_all_posts_for(name)
        counter_posts = len(list_of_posts)
        counter_bangok = 0
        for l in list_of_posts:
            if self.is_location_for_post(l, "Bangkok"):
                counter_bangok += 1
        if counter_bangok == counter_posts:
            return False
        else:
            return True
