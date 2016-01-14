""" Simple game. Deck deals cards. Some cards can be flipped.
    Some can't (see MAGIC_CARD) """

import pygame
from simple_cards import Deck, Card

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
FPS = 60
MAGIC_CARD = Card('Hearts', '7')
    

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.deck = self.load_deck()
        self.sprites = pygame.sprite.Group(self.deck)
        self.hand = []

    def load_deck(self):
        """ Create shuffled deck and place it on the screen (midtop) """
        deck = Deck()
        deck.shuffle()
        deck.rect.midtop = self.rect.midtop
        return deck

    def update_cards(self):
        """ Place cards in grid """
        x = 0
        y = WINDOWHEIGHT // 5
        gap = 5
        for card in self.hand:
            if x >= WINDOWWIDTH - card.rect.width + gap:
                y += card.rect.height + gap
                x = 0
            card.rect.topleft = (x, y)
            x += card.rect.width + gap

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # Close window
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:        # Mouse click
                self.click(pygame.mouse.get_pos())

    def click(self, position):
        """ Apply rules to clicked cards """
        if self.deck.rect.collidepoint(position):       # Deck deals card
            new_card = self.deck.deal()
            self.hand.append(new_card)
        for card in self.hand:
            if card.rect.collidepoint(position):        # Cards are clickable
                if card != MAGIC_CARD:         # But not all
                    card.flip()
                break

    def mainloop(self):
        while True:
            self.clock.tick(FPS)
            self.screen.fill((0, 0, 0))
            self.manage_events()
            self.update_cards()
            self.sprites.add(*self.hand)
            self.sprites.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    Game().mainloop()
