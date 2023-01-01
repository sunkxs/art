from datetime import datetime
import git
date = datetime.now()

repo = git.Repo('')

repo.index.add(['main.py', 'urandom.txt'])

message = """
   #####  #     # #     # #    #  #     #  ##### 
  #     # #     # ##    # #   #    #   #  #     #
  #       #     # # #   # #  #      # #   #      
   #####  #     # #  #  # ###        #     ##### 
        # #     # #   # # #  #      # #         #
  #     # #     # #    ## #   #    #   #  #     #
   #####   #####  #     # #    #  #     #  ##### 
""".strip().splitlines()

for y,line in enumerate(message):
    for x,char in enumerate(line):
        if char == "#":
            for i in range(y+1):
                print(x,y,char)
                with open("urandom.txt", "wb") as file:
                    with open("/dev/urandom", "rb") as random_file:
                        file.write(random_file.read(1000))
                        repo.index.commit('commit', author_date=datetime.strptime(f'2023-{x}-{y}', "%Y-%W-%w").isoformat())
                        
print("push")
repo.remotes.origin.push()


#28dec, måndagen med 1jan i veckan


