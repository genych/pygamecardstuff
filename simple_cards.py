""" Some cards to play with """

import pygame
from random import shuffle

SUITS = set(["Clubs", "Diamonds", "Hearts", "Spades"])
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# Fancy representation of ranks
RANKS = {key: value for value, key in enumerate(RANKS, start=1)}


class Card(pygame.sprite.Sprite):
    """ Simple card. Can be compared to other cards by rules of maumau.
        Must be in SUITS and RANKS """
    back = pygame.image.load('back.png')        # Same for all cards

    def __init__(self, suit, rank):
        super(Card, self).__init__()        
        self.suit = suit
        self.rank = rank
        self.closed = False
        self.face = self.get_image()
        self.image = self.face
        self.rect = self.image.get_rect()

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit) if not self.closed else '?'

    def __cmp__(self, other):
        return not (self.suit == other.suit or self.rank == other.rank)

    def get_image(self):
        return pygame.image.load(convert_card_to_filename(self.suit, self.rank))

    def flip(self):
        self.closed = not self.closed
        self.image = self.back if self.closed else self.face

class Deck(pygame.sprite.Sprite):
    """ New deck of cards. Don't forget to carefully shuffle it """
    image = pygame.image.load('deck.png')
    rect = image.get_rect()

    def __init__(self):
        super(Deck, self).__init__()
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def __str__(self):
        return 'Deck with %s cards' % len(self.deck)

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        if not self.deck:
            raise Exception('No cards left')
        return self.deck.pop()


def convert_card_to_filename(suit, rank):
    """ Validate card, return name of the image """
    if not (suit in SUITS and rank in RANKS):
        raise Exception('Error 404: Card "%s of %s" not found' % (rank, suit))
    prefix = suit[0].lower()
    suffix = '%02d' % RANKS[rank]
    extension = '.png'
    return ''.join((prefix, suffix, extension))
