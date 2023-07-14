import os
import time 
import click



def run_mqs():
  print("In docker...")
  print(os.environ["APP_ENV"])
  i = 0
  while True:
      i += 1
      print(i)
      time.sleep(10)
  

@click.group()
def cli(): pass

@cli.command("run-mqs")
def _cli_run_mqs():
   run_mqs()

if __name__ == "__main__":
   cli()