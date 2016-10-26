import os
import hashlib
import time

def generate_roles(num):
    pass


class Player:
    def __init__(self,uid=None):
        self.rid = None
        self.role = None
        self.uid = uid
        self.active = time.time()

    def get_uid(self):
        return self.uid

    def set_active(self):
        self.active = time.time()

    def get_active(self):
        return self.active;

    def set_role(self,role=None):
        if role == None:
            return False
        self.role = role
        return True

    def get_role(self):
        return self.role

    def set_rid(self,rid=None):
        if role == None:
            return False
        self.rid = rid
        return True

    def get_rid(self):
        return self.rid

class Room:
    def __init__(self,player=None):
        self.role = []
        self.rid = hashlib.md5(str(player.get_uid)+str(time.time())).hexdigest()
        self.playerlist = {}
        self.playerlist[player.get_uid] = player
        length = 1

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

class OnlinePlayer:
    def __init__(self):
        self.players = {}

    def add_player(self, uid=None):
        p = Player(uid)
        self.players['uid'] = p
#testing
if __name__ == "__main__":
    p = Player(uid='100040')
    r = Room(player=p)
