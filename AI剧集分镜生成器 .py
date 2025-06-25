# -*- coding: utf-8 -*-
"""
《异人之下》AI剧集智能生产系统 v2.0
包含：分镜表格生成器 + 图像提示词引擎 + 视频动态公式
"""
import random, datetime, csv
from tabulate import tabulate  # 需pip install tabulate

# ========================= 用户配置区 =========================
WORLD_VIEW = "赛博修真+量子江湖"  
MAIN_CONFLICT = "传统异人界与AI觉醒者的终极对决"  
MAIN_CHARACTER = "冯宝宝(纳米机甲版)"  

# ========================= 智能素材库 =========================
# 分镜要素库
SHOT_TYPES = ["全景", "中景", "特写", "大特写"]
ANGLES = ["俯拍", "仰拍", "水平跟拍", "荷兰角"]
MOVEMENTS = [
    "斯坦尼康环绕", "无人机俯冲", 
    "轨道横移", "手持抖动", "希区柯克变焦"
]
LIGHTINGS = ["赛博霓虹", "炁体流光", "全息粒子", "故障艺术"]

# 图像提示词库
STYLES = [
    "虚幻引擎5渲染", "赛博朋克水墨", 
    "吉卜力机械风", "黑魂式暗黑美学"
]
MATERIALS = [
    "半透明量子材料", "生锈的纳米装甲", 
    "流动的数据光纹", "破碎的全息投影"
]

# ========================= 核心生成器 =========================
class AIProductionSystem:
    def __init__(self):
        self.scene_counter = 1
        self.shot_counter = 1
        
    # 生成分镜表格
    def generate_storyboard(self, scene_count=3):
        """生成带表格格式的分镜脚本"""
        storyboard = []
        
        for _ in range(scene_count):
            scene_duration = random.randint(40, 90)
            scene_shots = random.randint(3, 6)
            
            for _ in range(scene_shots):
                shot_type = random.choice(SHOT_TYPES)
                angle = random.choice(ANGLES)
                movement = random.choice(MOVEMENTS)
                duration = random.randint(3, 8)
                
                # 动态生成画面描述
                visual_desc = f"{random.choice(LIGHTINGS)}中，{MAIN_CHARACTER}发动{random.choice(['数据化拘灵遣将','区块链金光咒'])}"
                dialogue = random.choice([
                    "咯老子今天要打十个！",
                    "你的异能...是复制粘贴噻？",
                    "莫挨老子，WiFi信号都被你切断了！"
                ])
                
                storyboard.append([
                    self.scene_counter,
                    self.shot_counter,
                    f"{shot_type}/{angle}",
                    movement,
                    visual_desc,
                    dialogue,
                    f"炁体流动声效+{random.choice(['二进制音效','古琴混音'])}",
                    duration
                ])
                self.shot_counter += 1
            self.scene_counter += 1
        
        # 表格输出
        headers = ["场号", "镜号", "SHOT", "运镜", "画面描述", "对白", "旁白/音效", "时长(s)"]
        return tabulate(storyboard, headers, tablefmt="grid")
    
    # 生成图像提示词
    def generate_image_prompt(self):
        """生成AI绘图提示词"""
        prompt_en = f"{random.choice(STYLES)}, {random.choice(['电影感全景','压迫性特写'])}, " \
                   f"{MAIN_CHARACTER}在{random.choice(['量子擂台','数据废墟'])}, " \
                   f"{random.choice(LIGHTINGS)}照明, {random.choice(['破损的机械臂','飘散的数据粒子'])}, " \
                   f"{random.choice(MATERIALS)}, 动态模糊特效, " \
                   f"Octane渲染, 8K分辨率, {random.choice(['悲壮史诗感','黑色幽默氛围'])}"
        
        prompt_cn = f"{random.choice(STYLES)}风格, {random.choice(['电影级全景','压迫感特写'])}景别, " \
                   f"拍摄主体:{MAIN_CHARACTER}位于{random.choice(['量子擂台','数据坟场'])}, " \
                   f"光线:{random.choice(LIGHTINGS)}, 形态:{random.choice(['断裂的纳米刀','飘散的代码碎片'])}, " \
                   f"材质:{random.choice(MATERIALS)}, 互动效果:能力发动瞬间, " \
                   f"专业术语:Octane渲染, 8K分辨率, 整体氛围:{random.choice(['悲壮史诗','赛博诙谐'])}"
        
        return prompt_en, prompt_cn
    
    # 生成视频动态公式
    def generate_video_prompt(self):
        """生成图生视频动态公式"""
        movements = ["环绕运镜", "急速推进", "慢速拉远", "手持抖动跟随"]
        actions = [
            "机甲关节展开武器系统", 
            "全息符咒矩阵旋转重组",
            "数据粒子凝聚成人形"
        ]
        results = [
            "镜头突然定格在武器充能特写",
            "画面分裂成多个数字化分身",
            "背景坍缩成二进制瀑布流"
        ]
        
        formula = f"{random.choice(movements)} + " \
                 f"{random.choice(actions)} + " \
                 f"{random.choice(results)}"
        
        return formula

# ========================= 执行输出 =========================
if __name__ == "__main__":
    print(f"⚙️ 《{WORLD_VIEW}:{MAIN_CONFLICT}》AI智能生产系统")
    print(f"🕶 主演:{MAIN_CHARACTER} | 生成时间:{datetime.datetime.now()}\n")
    
    system = AIProductionSystem()
    
    # 输出分镜表格
    print("🎬 分镜故事板")
    print(system.generate_storyboard())
    
    # 输出图像提示词
    print("\n🖼 AI图像提示词")
    img_en, img_cn = system.generate_image_prompt()
    print(f"英文提示词:\n```\n{img_en}\n```")
    print(f"中文描述:\n```\n{img_cn}\n```")
    
    # 输出视频动态公式
    print("\n🎥 图生视频公式")
    video_formula = system.generate_video_prompt()
    print(f"动态公式: {video_formula}")
    print(f"示例:『镜头推进 + 机甲关节展开武器系统 + 突然定格在充能核心特写』")

# ========================= 使用说明 =========================
"""
1. 安装依赖: 
   pip install tabulate

2. VSCode运行:
   - 复制本代码到.py文件
   - 按F5或右键"Run Python File"

3. 自定义修改:
   - 修改顶部WORLD_VIEW等参数
   - 调整素材库内容(如SHOT_TYPES)
   - 控制生成数量(scene_count)

4. 扩展建议:
   - 添加CSV导出功能
   - 集成Stable Diffusion API
   - 增加GUI界面
"""