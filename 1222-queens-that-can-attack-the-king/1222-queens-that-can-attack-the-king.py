class Solution:
    def choose_nearest(self, pos1, pos2, pivot):
        if pos1 == None:
            return pos2

        elif pos2 == None:
            return pos1

        x1, y1 = pos1
        x2, y2 = pos2
        a, b = pivot

        if (x1 - a) ** 2 + (y1 - b) ** 2 < (x2 - a) ** 2 + (y2 - b) ** 2:
            return pos1

        return pos2

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        king_x = king[0]
        king_y = king[1]


        positions = {
            "top" : None,
            "bottom" : None,
            "right"  : None,
            "left"  : None,
            "top_left"  : None,
            "top_right"  : None,
            "bottom_left"  : None,
            "bottom_right" : None
        }

        for queen_x, queen_y in queens:
            queen = [queen_x, queen_y]
            dx = queen_x - king_x
            dy = queen_y - king_y

            top = positions['top']
            bottom = positions['bottom']
            right = positions['right']
            left = positions['left']
            top_left = positions['top_left']
            top_right = positions['top_right']
            bottom_left = positions['bottom_left']
            bottom_right = positions['bottom_right']

            # on same column
            if dx == 0:                
                # queen is above king
                if dy < 0:
                    positions["top"] = self.choose_nearest(top, queen, king)

                # queen is below king
                elif dy > 0:
                    positions["bottom"] = self.choose_nearest(bottom, queen, king)

            # on same row
            elif dy == 0:
                # queen to left of king
                if dx < 0:
                    positions["left"] = self.choose_nearest(left, queen, king)
                # queen to right of king
                elif dx > 0:
                    positions["right"] = self.choose_nearest(right, queen, king)

            # on diagonal
            elif abs(dx) == abs(dy):
                # top left                 
                if dx < 0 and dy < 0:
                    positions["top_left"] = self.choose_nearest(top_left, queen, king)

                # top right                 
                elif dx > 0 and dy < 0:
                    positions["top_right"] = self.choose_nearest(top_right, queen, king)

                # bottom left
                elif dx < 0 and dy > 0:
                    positions["bottom_left"] = self.choose_nearest(bottom_left, queen, king)

                # bottom right                 
                elif dx > 0 and dy > 0:
                    positions["bottom_right"] = self.choose_nearest(bottom_right, queen, king)

        output = []
        for v in positions.values():
            if v:
                output.append(v)


        return output