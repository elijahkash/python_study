from typing import List, Dict


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # Stupid Brute Force (out of time)
        # i = 1
        # while i < len(folder):
        #     j = 0
        #     while j < i:
        #         if (len(folder[i]) > len(folder[j])
        #            and folder[j] == folder[i][:len(folder[j])]
        #            and folder[i][len(folder[j])] == '/'):
        #             folder = folder[:i] + folder[i + 1:]
        #             i -= 1
        #             break
        #         elif (len(folder[j]) > len(folder[i])
        #               and folder[i] == folder[j][:len(folder[i])]
        #               and folder[j][len(folder[i])] == '/'):
        #             folder = folder[:j] + folder[j + 1:]
        #             i -= 1
        #         else:
        #             j += 1
        #     i += 1
        # return folder

        # Folder tree (recursive)

        def add_in_tree(tree: Dict[str, Dict], path: List[str]) -> None:
            if len(path) == 1 and path[0] in tree:
                tree[path[0]] = {}
            elif path[0] not in tree:
                tmp = tree
                while path:
                    tmp[path[0]] = {}
                    tmp = tmp[path[0]]
                    path = path[1:]
                return
            elif tree[path[0]] == {}:
                return
            else:
                add_in_tree(tree[path[0]], path[1:])

        def collect_folders(tree: Dict[str, Dict],
                            res: List[str], cur: str) -> None:
            if not tree:
                res.append(cur)
                return
            for item, subitems in tree.items():
                collect_folders(subitems, res, cur + '/' + item)

        tree: Dict[str, Dict] = {}
        for item in folder:
            add_in_tree(tree, item[1:].split('/'))
        res: List[str] = []
        collect_folders(tree, res, '')
        return res
