"""In a standard deck of cards, there are 13 of each suit. There are numbered cards (from 2 to 10) 
and face cards (Jack, Queen, King, and Ace). If we were to rank the face cards, Jack would be 11, 
Queen 12, King 13, and the Ace 14.

Write a program that calculates the average rank of one hand of cards. 
Don't forget to consider the rank of the face cards."""

cards = dict{"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":11, "Queen":12, "King":14}
sum = 0
count = 0

while (count < 6):
    input 
