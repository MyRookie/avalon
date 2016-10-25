import os
import hashlib
import time

def generate_roles(num):
    pass


class player:
    def __init__(self,uid=None):
        if uid == None:
            return False
        self.role = None
        self.uid = uid
        return True

    def get_role(self):
        return self.role

    def get_uid(self):
        return self.uid

    def set_role(self,role=None):
        if role == None:
            return False
        self.role = role
        return True

class room:
    def __init__(self,player=None):
        if player == None:
            return False
        self.role = []
        self.rid = hashlib.md5(str(player.get_uid)+str(time.time())).hexdigest()
        self.playerlist = {}
        self.playerlist[player.get_uid] = player
        length = 1
        return True;

    def get_length(self):
        return length

    def get_rid(self):
        return self.rid

    def get_players(self):
        return self.playerlist

    def add_player(self,player=None):
        if player == None:
            return False
        self.playerlist[player.get_uid] = player
        self.length += 1
        return True

    def remove_player(self,uid=None):
        if uid == None:
            return False
        del self.playerlist[uid]
        self.length -= 1
        return True

    def start_game(self):
        if self.length > 10 or self.length < 6:
            return False
        self.role = generate_roles(self.length)
        idx = 0
        for uid in self.playerlist:
            self.playerlist[uid].set_role(self.role[idx])
            idx += 1
        return True
