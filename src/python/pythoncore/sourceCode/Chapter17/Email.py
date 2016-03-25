# coding:utf-8

from poplib import  POP3

pop3 = POP3('pop.163.com')
pop3.user('cjopengler@163.com')
pop3.pass_('hawk1qaz2wsx')

rsp, msg, siz = pop3.retr(pop3.stat()[0] - 1)
# strip headers and compare to orig msg
# sep = msg.index('')
# recvBody = msg[sep+1:]

print msg
pop3.quit()
