class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = {(0, 0)}
        x = y = 0
        for character in path:
            match character:
                case "N":
                    y += 1
                case "E":
                    x += 1
                case "W":
                    x -= 1
                case "S":
                    y -=1
            if (x, y) in locations: return True
            locations.add((x, y))
        return False