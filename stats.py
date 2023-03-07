class Stats():
    """отслеживает статистику"""
    
    def __init__ (self):
        """инициплизируемся"""
        self.reset_stats()
        
    def reset_stats(self):
        """Статистика которая меняется во врем игры"""
        self.gun_left = 2