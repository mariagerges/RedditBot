import praw
import random
import datetime
import time
from textblob import TextBlob


# FIXME:
# copy your generate_comment functions from the week_07 lab here


# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jmk23d/another_goodie_from_tiedrich/'
submission = reddit.submission(url=reddit_debate_url)


for i in range (1000):
    def generate_comment_0():
        names = ['Biden', 'Joe Biden', 'Mr. Biden', 'Joseph Robinette Biden Jr.', 'Dr. Biden']
        name = random.choice(names)

        jobs = ['president', 'President of the United States', 'United States President', 'Chief Executive of the United States', 'ruler of the United States']
        job = random.choice(jobs)

        shoulds = ['should be', 'must be', 'better be', 'ought to be' , 'shall' ]
        should = random.choice(shoulds)

        advs = ['healthcare', 'equity', 'equality', 'human rights', 'anti-racism']
        adv = random.choice(advs)

        everyones = ['everyone' + 'every american' + 'the american people' + 'americans' + 'every citizen']
        everyone = random.choice(everyones)

        text = name + " " + should + " " + job + ' because he supports ' + adv + ' for ' + everyone + ' . ' + ' Go Vote for Biden!! '
        return text 


    def generate_comment_1():
        supports = ['supporting' , 'aiding', 'assisting', 'helping', 'working for']
        support = random.choice(supports)

        senators = ['senator' + 'legislator' + 'congressman' + 'political figure' + 'senate member']
        senator = random.choice(senators)

        elections = ['election' + 'the poll' + 'the vote' + 'the general election' 'referendum']
        election = random.choice(elections)

        names = ['Biden', 'Joe Biden', 'Mr. Biden', 'Joseph Robinette Biden Jr.', 'Dr. Biden']
        name = random.choice(names)

        jobs = ['president', 'President of the United States', 'United States President', 'Chief Executive of the United States', 'ruler of the United States']
        job = random.choice(jobs)

        text = name + " has a long history of " + support + " union and workers'rights. When he first took office as a " + senator + " , he called for public financing of " + election + " . Biden helped secure the passage of billions of dollars in funding to build out broadband and make other job-creating infrastructure investments. Vote Biden for " + job + " !! "
        return text 

    def generate_comment_2():
        
        covids = ["COVID-19" + "Corona" + "Coronavirus disease" + "Coronavirus" + "Covid"] 
        covid = random.choice(covids)

        votes = [' vote for ' + ' pick ' + ' choose ' + " go for " + " yes for " ]
        vote = random.choice(votes)

        responds = ['respond to' , 'deal with' , 'manage' , 'cope with', 'sucessfully pass']
        respond = random.choice(responds)

        vaccines = ['vaccination', 'immunization' , 'serum', 'inoculation', 'vaccine']
        vaccine = random.choice(vaccines)

        usas = ["USA's " , "America's" , "The United States'", "our nation's" + "our great country's"]
        usa = random.choice(usas)

        text = " Biden knows how to " + respond + " a public health crisis and has the experience we need to deal with " + covid + " . He led " + usa +  " successful response to Ebola by listening to scientists and following the facts. Supports cost-free COVID-19 testing, treatment, preventative services, and eventual " + vaccine + " for the insured and uninsured. Backs premium pay for essential workers. " + vote + " Biden!! "
        return text 

    def generate_comment_3():
        names = ['Trump', "Dr . Trump", 'Mr. preisdent', 'Donald John Trump', 'Donald Trump']
        name = random.choice(names)

        truths = ['truth' , 'facts' , 'realities' , 'actualities']
        truth = random.choice(truths)

        americans = ['american citizens' , 'americans', 'our citizens', 'we', 'an american citizen']
        american = random.choice(americans)

        jobs = ['president', 'President of the United States', 'United States President', 'Chief Executive of the United States', 'ruler of the United States']
        job = random.choice(jobs)

        hoaxs = ['a hoax', 'not true' , 'a propaganda', 'a lie', 'a joke']
        hoax = random.choice(hoaxs)

        text = " Politicians always stretch the " + truth + " , but " + american + " expect their " + job + " to level with them. " + name + " not only lies, but doubles down on those lies. Examples include saying that Muslims in New Jersey cheered 9/11, that vaccines cause autism, that President Obama wasn’t born in the United States and that global warming is " + hoax + " perpetrated by China to close U.S. factories. "
        return text 

    def generate_comment_4():
        insults = ['insults women', 'disrespect women', 'disreagrd women' + 'ridicule women', 'discorn women']
        insult = random.choice (insults)

        mays = ['may not be', 'should not be', 'must not be', 'ought not to be', 'must be prevented to be']
        may = random.choice(mays)

        americans = ['Generations of American', 'many american', 'a lot of american', 'multiple american']
        american = random.choice(americans)

        grows = ['to grow up to be President' , 'to study hard to be president' , 'to work hard to be president', 'to aim to be president', 'to look forward to being president']
        grow = random.choice(grows)

        anyones = ['anyone' , 'everyone' , 'each person', 'each citizen', 'any indvidual']
        anyone = random.choice (anyones)

        text = american + " parents have inspired their children " + grow + " . But a would-be President who " + insult + " , spews profanity, is on his third wife, and calls " + anyone + " who disagrees with him a “loser” " + may + " someone to look up to."
        return text 

    def generate_comment_5():
        advisers = ['advisers' , 'helpers', 'thinkers', 'consultants'] 
        adviser = random.choice(advisers)

        govs = ['governments' , 'countries', 'large adminstrations', 'big authorities']
        gov = random.choice(govs)

        names = ['Trump', "Dr . Trump", 'Mr. preisdent', 'Donald John Trump', 'Donald Trump']
        name = random.choice(names)

        knows = ['did not know', 'had no idea', 'had no clue', 'was not infomred about', 'did not have any info']
        know = random.choice(knows)

        understands = ['know' , 'understand' , 'have an idea about how', 'realize', 'see']
        understand = random.choice(understands)

        text = " Even with the best " + adviser + " ,  a president needs to " + understand + " how " + gov + " operates. " + name + ' ' + know + " what the nuclear triad was when asked in December’s debate, nor in November’s debate that China wasn’t a party to the Trans-Pacific Partnership, which is intended to counter that country’s economic influence."
        return text 

    def create_result():  #create a string
        result = ""    
        options = [0,1,2,3,4,5]
        choice = random.choice(options)
        if choice == 0:
            result = generate_comment_0()
        elif choice == 1:
            result = generate_comment_1()
        elif choice == 2:
            result = generate_comment_2()
        elif choice == 3:
            result = generate_comment_3()
        elif choice == 4: 
            result = generate_comment_4()
        else:
            result = generate_comment_5()
        return result

    def generate_comment(s):
        submission.reply(s)

    
    # each iteration of this loop will post a single comment;
    # since this loop runs forever, your bot will continue posting comments forever;
    # (this is what makes it a deamon);
    # recall that you can press CTRL-C in the terminal to stop your bot
    #
    # HINT:
    # while you are writing and debugging your code, 
    # you probably don't want it to run in an infinite loop;
    # you can change this while loop to an if statement to make the code run only once
    #if True:
        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    
        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit = None)
    all_comments = []
    for comment in submission.comments:
        #if type(comment) is praw.models.reddit.comment.Comment:
        all_comments.append(comment)
    for comment in submission.comments.list():
        if type(comment) is praw.models.reddit.comment.Comment: 
            all_comments.append(comment)
        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments o remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    my_comments = []
    for comment in submission.comments:
        if comment.author != "CS40BOT":
            not_my_comments.append(comment)
        else: 
            my_comments.append(comment)                       
        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))
    print('len(my_comments)=',len(my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (you bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    comments_without_replies = []
    comments_with_replies = []
    has_replied = None
    if has_not_commented == True:
        generate_comment(create_result())
            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
    else:
        for comment in not_my_comments:
            has_replied = False
            for reply in comment.replies:
                if str(reply.author) == 'CS40BOT':
                    has_replied = True
            if has_replied == True:    
                comments_with_replies.append(comment)
            else:
                comments_without_replies.append(comment)          

            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over not_my_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))
        print('len(comments_with_replies)=',len(comments_with_replies))

    
            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
        try:        
            random_comment = random.choice(comments_without_replies)
            result1 = create_result()
            random_comment.reply(result1)
            print (result1)
        except IndexError:
            pass    
            # FIXME (task 5): select a new submission for the next iteration;
            # your newly selected submission should have a 50% chance of being the original submission
            # (url in the reddit_debate_url variable)
            # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
            # HINT: 
            # use random.random() for the 50% chance,
            # if the result is less than 0.5,
            # then create a submission just like is done at the top of this page;
            # otherwise, create a subreddit instance for the csci40 subreddit,
            # use the .top() command with appropriate parameters to get the list of all submissions,
            # then use random.choice to select one of the submissions 
    value = random.random()
    total_submissions = list(reddit.subreddit('csci040temp').top(time_filter='all'))
    if value < 0.5:
        submission = reddit.submission(url=reddit_debate_url)
    else: 
        choice = random.choice(total_submissions)
        submission = reddit.submission(choice)
        print ('choice=' , choice)


#extra upvote and downvote comments 

for comment in submission.comments.list():
    chosen_comment = TextBlob(comment.body)
    polarity = chosen_comment.sentiment.polarity
    if 'biden' in comment.body.lower() and polarity < 0:
        comment.downvote()
        print ('comment downvote')
    if 'biden' in comment.body.lower() and polarity >= 0:
        comment.upvote()
        print ('comment upvote')
print ('done')

#extra upvote submissions

for submission in reddit.subreddit('csci040temp').hot(limit = None):
    chosen_submission = TextBlob(submission.title)
    polarity = chosen_submission.sentiment.polarity   
    if 'biden' in submission.title.lower() and polarity >= 0:
        submission.upvote()
        print ('upvote submission')
    if 'biden' in submission.title.lower() and polarity < 0: 
        submission.downvote()
        print ('downvote submission') 
print ('done')          

          
for comment in submission.comments.list():
    chosen_comment = TextBlob(comment.body)
    polarity = chosen_comment.sentiment.polarity
    if 'trump' in comment.body.lower() and polarity < 0:
        comment.upvote()
        print ('comment upvote')
    if 'trump' in comment.body.lower() and polarity >= 0:
        comment.downvote()
        print ('comment downvote')   

for submission in reddit.subreddit('csci040temp').hot(limit = None):
    chosen_submission = TextBlob(submission.title)
    polarity = chosen_submission.sentiment.polarity   
    if 'trump' in submission.title.lower() and polarity >= 0:
        submission.downvote()
        print ('downvote submission')
    if 'trump' in submission.title.lower() and polarity < 0: 
        submission.upvote()
        print ('upvote submission')   