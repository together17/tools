#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys
import os

base_dir = ''

def cp_without_dotgit(src_dir, dest_dir):
  if not src_dir.endswith('/'):
    src_dir +='/'
  print (src_dir)
  print (dest_dir)
  if not dest_dir.endswith('/'):
    dest_dir +='/'
 
  entry_list = os.listdir(src_dir)
  print(entry_list)
  for entry in entry_list:
    entry_path = src_dir + entry
    if entry != '.git':
       if os.path.isdir(entry_path):
          target_dir = entry_path.replace(src_dir,'').strip('/')
          print('-------"%s" '%target_dir)
          target_dir = dest_dir + target_dir
          cmd = 'mkdir "%s"'%target_dir
          os.system(cmd)
          cp_without_dotgit(entry_path, target_dir)
       elif os.path.isfile(entry_path):
           target_file = entry_path.replace(src_dir,'').strip('/')
           print('dest_dir: "%s"  target file:"%s"'%(dest_dir,target_file))
           target_file = dest_dir + target_file
           cmd = 'cp "%s" "%s"' %(entry_path,target_file)
           os.system(cmd)
       else:
          pass

def main():
  if len(sys.argv) !=3:
     print ("usage: python cp_pure_git_repos.py source_dir target_dir")
     return
  src_dir = os.path.abspath(sys.argv[1])
  if not src_dir.endswith('/'):
    src_dir +='/'
  dest_dir = os.path.abspath(sys.argv[2])
  if not dest_dir.endswith('/'):
    dest_dir +='/'
  global base_dir
  #print('dest_dir: "%s"  src file:"%s"'%(dest_dir,src_dir))
  base_dir = src_dir
  cp_without_dotgit(src_dir,dest_dir)

if __name__ == '__main__':
  main()
