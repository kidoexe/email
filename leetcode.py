class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1

#k აკონტროლებს რიცხვების მდებარეობას, თუ რიცხვი ნოლი არ არის ის იწევა მარცხნივ ხოლო ნოლი გადადის მარჯვნივ :3