class Stats():
    """отслеживает статистику"""
    
    def __init__ (self):
        """инициплизируемся"""
        self.reset_stats()
        self.run_game = True
        with open('hiscore.txt', 'r') as f:
            self.hiscore = int(f.readline())
        
        
    def reset_stats(self):
        """Статистика которая меняется во врем игры"""
        self.gun_left = 2
        self.score = 0
        
        