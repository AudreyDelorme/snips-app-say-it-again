#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the result sentences and intents for the French version
of the Say it again skill.
"""

# Result sentences
RESULT_SAY_SORRY = "Désolé, je ne me souviens pas de ce que j'ai dit. Je dois m'être endormi."
RESULT_TEXT_SORRY = "Désolé, je ne me souviens pas de ce que vous avez dit. Je dois m'être endormi."
RESULT_TEXT = "J'ai entendu: \"{0}\" avec une probabilité de {1}."
RESULT_TEXT_NOTHING = "Désolé, je n'ai rien entendu."
RESULT_INTENT_SORRY = "Désolé, je ne me souviens pas de la dernière action. Je dois m'être endormi"

#Result sentences coffee
RESULT_SAY_MAX = "Je n'ai la capacité de vous faire que deux cafés maximum, sinon va chez starbucks !"
RESULT_TEXT_UN_CAFE = "Et c'est parti pour un café"
RESULT_TEXT_CAFE_LONGUEUR = "Je vais vous servir un {2} café."
RESULT_TEXT_DEUX_CAFES = "Je vous prépare tout de suite deux cafés"
RESULT_TEXT_CAFES_LONGUEUR = "Je vais vous servir deux {2} café."
RESULT_TEXT_CAFE_IO = "Haaaaaaaa, pardon je viens de bailler"
RESULT_TEXT_CAFE_NETTOIE = "je me rince, merci de patienter"
RESULT_TEXT_CAFE_VAPEUR = "attention je vais faire de la vapeur.... tchou tchou ! "

# Intents
INTENT_SAY_IT_AGAIN = "hermes/intent/Tealque:SayItAgain"
INTENT_WHAT_DID_I_SAY = "hermes/intent/Tealque:WhatDidISay"
INTENT_REPEAT_ACTION = "hermes/intent/Tealque:RepeatAction"
INTENT_NETTOIE = "hermes/intent/Tealque:Nettoie2"
INTENT_VAPEUR = "hermes/intent/Tealque:Vapeur2"
INTENT_VERSER = "hermes/intent/Tealque:Verser2"
INTENT_CAFE_IO = "hermes/intent/Tealque:Cafe_io2"
