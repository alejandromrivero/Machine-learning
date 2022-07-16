import re
from collections import defaultdict, Counter
import math
import glob, re, random

import pandas as pd

from machine_learning import split_data


def tokenize(message):
    message=message.lower()
    all_words=re.findall("[a-z0-9]+",message)
    return set(all_words)


texto="After several months in Maintenance Mode, their website's domain and that of their only lodge are both now up for sale by a domain broker. Prior to that, it hadn't been updated since 2012 (their first entry was looking forward to a successful 2013 - but obviously THAT didn't work out). The only (nominal) connection GOFUS had left seemed to be a website created by the group's founder (no longer a leader, as far as anyone admits) and composed almost exclusively of purloined material from re-tweets automatically posted, coming from legitimate lodges and other Masonic bodies but even that has ceased. Their American Masonic Alliance (a tortured self-created entity to show how many groups they were connected to) is completely gone and even their SETI account (which they at one time reluctantly admitted was the only basis for their claim of 'public service') shows nobody even has a computer doing that in the background anymore. We'd comment Oh, how the mighty have fallen! but from our perspective, they never were mighty in the first place....There's no victory dance going on here at masonicinfo.com: the bold, brash, sometimes foul behavior exhibited by the leadership who felt they could take control of world-wide Freemasonry from behind a computer at an anesthesia business office in Georgia was completely absurd from the outset. What was the most troubling, though, were the constant lies, prevarication and obfuscation used by ALL of those involved, taking the group so far from the principles of Freemasonry. Although at the outset, some of the founder's ideas seemed - to some - to have a nominal amount of merit, the self-aggrandizement and blatant falsehoods quickly allowed the true nature of their actions to be seen in the harsh light of reality. Did we call it correctly right from the start, way back in those early days on alt.freemasonry when we first outed the pseudonyms and blew apart the ridiculous claims? Yep - and we'll take full credit for it when others - including some friends and Brothers - felt that we'd been too tough on Jeff and Company. Nevertheless, it was - for us at least - easy to see where it would end up. Now, with a trail of broken-hearted (and in several cases, broken-wallet) acolytes kicked to the curb, there's really no redeeming accomplishment, of even the slightest, as far as we can tell. From their first days of demanding a college degree (when their founder, it was later reported, didn't have one) on through their recruiting for members on an anti-Semitic newsgroup, to the takeover of a moribund lodge and its property with the constant lies about legitimacy of legacy and the bizarre connection with a French irregular so-called 'Grand Lodge', it was all a farce writ large. And yes, we documented every step - and had FAR more material about their aberrations than we ever made public. Was it OUR fault that this group was created (like it says in the header)? Of course not, but that was just one more example in a sad series of ludicrous self-justifications for their bad behavior. Now gone, they will likely not even be a footnote in Masonic history. If only half of the sycophants had spent half the time, money, and energy they spent on GOOFUS stupidity doing something for their families or communities, the would could have been a better place today. Thus wastes man....  Goodbye, GOOFUS: we hardly knew thee - thank goodness! The continuing lies leading to obscurity. In a Bob Dylan musical classic there's a line:When you got nothing, you got nothing to lose. And so the so-called Grand Orient of the United States as they seem to fade from consciousness. Websites falling away as domain registration renewals come due: apparently even the $15 or so is too much to waste on something non-existent. Members, what precious few there were, realize that time spent on trying to pretend that there's an organization in full bloom met with disdain from friends and scorn from family (if they have either still hanging in there with them). We particularly enjoyed this announcement which appeared sometime in 2013, one of their very few that year. Apparently they just didn't have time to list all of their many Grand Officers, to recognize the important contributions being made. It's a shame: Grand Wardens are the #2 and #3 elected officers (#3 and #4 in many Grand Lodges where they've got more than a dozen people and can have a Deputy Grand Master, unlike the GOOFUS folks apparently) and yet they don't even get their names on the website. What a shame....  (Oh, and did you notice: NONE of their blog/website postings are dated any longer. Golly: why is that, one wonders.... Hmmmmm....) ..blossoming into the future form of all American Freemasonry. Oh, come on: get a grip on reality, will you boys?"

def count_words(training_set):
    counts=defaultdict(lambda:[0,0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1]+=1
        return counts

def word_probabilities(counts,total_spam, total_non_spams,k=0.5):
    return [(w,
             (spam+k)/(total_spam+2*k),(non_spam+k)/(total_non_spams+2*k))
            for w,(spam, non_spam) in counts.iteritems()]
def spam_probability(word_probs,message):
    message_words=tokenize(message)
    log_prob_if_spam=log_prob_if_not_spam=0.0
    for word, prob_if_spam,prob_if_not_spam in word_probs:
        if word in message_words:
            log_prob_if_spam+=math.log(prob_if_spam)
            log_prob_if_not_spam+=math.log(prob_if_not_spam)
        else:
            log_prob_if_spam+=math.log(1.0-prob_if_spam)
            log_prob_if_not_spam+=math.log(1.0-prob_if_not_spam)
    prob_if_spam=math.exp(log_prob_if_spam)
    prob_if_not_spam=math.exp(log_prob_if_not_spam)
    return prob_if_spam/(prob_if_spam+prob_if_not_spam)


class NaivebayesClassifier:
    def __init__(self, k=0.5):
        self.k=k
        self.word_probs=[]
    def train(self, training_set):
        num_spams=len([is_spam
                       for message, is_spam in training_set
                       if is_spam])
        num_non_spams=len(training_set)-num_spams
        word_counts=count_words(training_set)
        self.word_probs=word_probabilities( word_counts,
                                           num_spams,
                                           num_non_spams,
                                           self.k)
    def classify(self,message):
        return spam_probability(self.word_probs,message)

path=r"F:/spam/*/*"
data=[]
for fn in glob.glob(path):
    is_spam='ham' not in fn
    with open(fn,'r') as file:
        for line in file:
            if line.startswith("Subject:"):
                subject=re.sub(r"^Subject: ","", line).strip()

                data.append((subject, is_spam))



random.seed(0)
train_data,test_data=split_data(data,0.5)

classifier=NaivebayesClassifier()
classifier.train(train_data)

classified=[(subject, is_spam,classifier.classify(subject))
            for subject, is_spam in test_data]
counts=Counter((is_spam,spam_probability>0.5)
               for _,is_spam,spam_probability in classified)

