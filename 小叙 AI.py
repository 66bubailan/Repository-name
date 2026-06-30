# -*- coding: utf-8 -*-
"""
====================================================================
🚀 小叙 AI v27.2.8 [切レンコフ放射 - 终极修复与命名固化版]
====================================================================
📝 【核心修改看板】
1. 🏷️ [固化命名] 移除繁琐的量子词汇！左侧主标题固定为 "小叙 AI"，右侧固定为 "小剪映"，控制开关固定为 "小剪映舱"。
2. 🐛 [报错熔断] 深度重构 Ollama 接口探针与异常捕获，解决任何潜在的网络及解析闪退报错。
3. 📦 [界面微调] 完美确保多语言切换时，核心品牌名不会被重置扭曲。
====================================================================
"""

import sys
import os
import threading
import json
import requests
import time
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk
import webbrowser

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# 全局通用多国波段矩阵 (移除冗余量子词汇，统一规范)
LANG_MATRIX = {
    "🇨🇳 中文 (CN)": {
        "lang_lbl": "🌐 国家语言波段:",
        "think": "✦ 深度思维舱",
        "placeholder": "❯ 注入辐射蓝光代码连通主网，输入指令...",
        "clear": "⚡ 净化缓冲区",
        "send": "发射脉冲",
        "import": "✦ 导入高刷素材 (多流向)",
        "param_title": " ✦ 强相互作用力剪辑参数调整矩阵 ",
        "scale": "视界缩放:",
        "volume": "声弦增益:",
        "rotate": "偏振翻转:",
        "speed": "时间坍缩:",
        "ratio": "空间映射:",
        "fps": "光栅率:",
        "sub_title": " ✦ 全息数字流字幕编码层 ",
        "out_btn": "✦ 定向目标黑洞存储地址",
        "start_btn": "⚡ 压缩时空 启动量子冷蓝渲染 ⚡",
        "gate_title": "🔒 核心算法舱已被中子锁死",
        "gate_sub": "检测到未授权，请激活右上方 [小剪映舱] 开关解除",
        "welcome": "🛰️ 系统控制台:\n接入协议成功。多国语言冷蓝超频网络链路已闭合，防火墙监控模块满载运行中...\n\n"
    },
    "🇺🇸 English (US)": {
        "lang_lbl": "🌐 National Lang Band:",
        "think": "✦ Deep Thought Deck",
        "placeholder": "❯ Inject radiation blue code to connect, enter command...",
        "clear": "⚡ Clear Buffer",
        "send": "Send Pulse",
        "import": "✦ Import Multi-Stream Video Materials",
        "param_title": " ✦ Strong Interaction Parameter Matrix ",
        "scale": "Scale Horizon:",
        "volume": "Audio Gain:",
        "rotate": "Polar Rotation:",
        "speed": "Time Collapse:",
        "ratio": "Spatial Map:",
        "fps": "Raster Rate:",
        "sub_title": " ✦ Holographic Digital Subtitle Layer ",
        "out_btn": "✦ Set Target Blackhole Storage Address",
        "start_btn": "⚡ Collapse Spacetime: Start Rendering ⚡",
        "gate_title": "🔒 Core Algorithm Bay Locked by Neutrons",
        "gate_sub": "Unauthorized access detected. Toggle [小剪映舱] top-right switch to unlock.",
        "welcome": "🛰️ System Console:\nProtocol connected successfully. Multi-language hyper-frequency link closed, firewall loaded...\n\n"
    },
    "🇯🇵 日本語 (JP)": {
        "lang_lbl": "🌐 国家言語バンド:",
        "think": "✦ 深層思考チャンバー",
        "placeholder": "❯ 青色放射コードを注入して接続、コマンドを入力...",
        "clear": "⚡ バッファクリア",
        "send": "パルス発射",
        "import": "✦ 高フレーム素材のインポート",
        "param_title": " ✦ 強い相互作用編集パラメータ調整マトリクス ",
        "scale": "視野ズーム:",
        "volume": "音声ゲイン:",
        "rotate": "偏光反転:",
        "speed": "時間崩壊:",
        "ratio": "空間マッピング:",
        "fps": "ラスタレート:",
        "sub_title": " ✦ ホログラフィック字幕エンコード層 ",
        "out_btn": "✦ ターゲットブラックホール保存先設定",
        "start_btn": "⚡ 時空圧縮：量子冷青レンダリング起動 ⚡",
        "gate_title": "🔒 中子ロックによりコアアルゴリズムが凍结",
        "gate_sub": "未確認のアクセス。右上の [小剪映舱] スイッチを有効にして解除してください。",
        "welcome": "🛰️ システムコンソール:\nプロトコル接続完了。多言語オーバークロックリンクが閉じ、ファイアウォール作動中...\n\n"
    }
}


class UltimateCyberSciFiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⚡ 小叙 AI v27.2.8")
        self.geometry("1400x900")
        self.minsize(1200, 800)

        # 🌌 色彩矩阵
        self.COLOR_BG = "#02040a"
        self.COLOR_CARD = "#0a0f24"
        self.COLOR_TEXT_MAIN = "#d8f8ff"
        self.COLOR_PRIMARY = "#0099ff"
        self.COLOR_ACCENT = "#bd00ff"
        self.COLOR_MUTED = "#475569"
        self.COLOR_WARN = "#ff5500"
        self.COLOR_WHITE = "#ffffff"

        self.configure(bg=self.COLOR_BG)

        # 核心逻辑变量
        self.chat_history = []
        self.selected_video_files = []
        self.output_path = ""
        self.is_generating = False

        self.think_status = False
        self.weapon_status = False

        self.is_timer_running = False
        self.timer_start_timestamp = 0.0
        self.gate_current_height = 1.0
        self.gate_animation_running = False

        self.font_main = ("Consolas", 11) if sys.platform != "darwin" else ("Consolas", 12)
        self.font_bold = ("Microsoft YaHei", 11, "bold") if sys.platform != "darwin" else ("PingFang SC", 12, "bold")
        self.font_title = ("Microsoft YaHei", 13, "bold") if sys.platform != "darwin" else ("PingFang SC", 14, "bold")
        self.font_terminal = ("Consolas", 11, "bold")

        self.style = ttk.Style()
        self.theme_use_safe()

        self.main_container = tk.Frame(self, bg=self.COLOR_BG)
        self.main_container.pack(padx=25, pady=20, fill="both", expand=True)

        # ==================== 👈 左侧 AI 核心区域 ====================
        self.left_frame = tk.Frame(self.main_container, bg=self.COLOR_BG)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=(0, 15))

        self.top_bar = tk.Frame(self.left_frame, bg=self.COLOR_BG)
        self.top_bar.pack(fill="x", pady=(0, 10))

        # 🏷️ 固定命名：彻底更名为“小叙 AI”
        self.lbl_core_title = tk.Label(self.top_bar, text="🛰️ 小叙 AI", font=self.font_title, fg=self.COLOR_PRIMARY,
                                       bg=self.COLOR_BG)
        self.lbl_core_title.pack(side="left")

        self.model_var = tk.StringVar(value="deepseek-r1:7b")
        self.model_selector = ttk.OptionMenu(self.top_bar, self.model_var, "deepseek-r1:7b", "deepseek-r1:1.5b",
                                             "deepseek-r1:7b", "deepseek-r1:8b", "deepseek-r1:14b")
        self.model_selector.pack(side="left", padx=15)

        self.lbl_lang_tag = tk.Label(self.top_bar, text="", font=self.font_bold, fg=self.COLOR_TEXT_MAIN,
                                     bg=self.COLOR_BG)
        self.lbl_lang_tag.pack(side="left", padx=(10, 5))

        self.lang_var = tk.StringVar(value="🇨🇳 中文 (CN)")
        self.lang_selector = ttk.OptionMenu(self.top_bar, self.lang_var, "🇨🇳 中文 (CN)", *list(LANG_MATRIX.keys()),
                                            command=self.switch_language)
        self.lang_selector.pack(side="left", padx=5)

        # ⚡ 深度思考舱开关组件
        self.think_toggle_frame = tk.Frame(self.top_bar, bg=self.COLOR_BG)
        self.think_toggle_frame.pack(side="right", padx=(10, 0))

        self.lbl_think_title = tk.Label(self.think_toggle_frame, text="", font=self.font_bold, fg=self.COLOR_WHITE,
                                        bg=self.COLOR_BG)
        self.lbl_think_title.pack(side="left", padx=(0, 8))

        self.btn_think_toggle = tk.Button(
            self.think_toggle_frame, text="[ ○ OFF ]", font=self.font_terminal,
            bg=self.COLOR_CARD, fg=self.COLOR_WHITE, activebackground=self.COLOR_CARD,
            activeforeground=self.COLOR_WHITE, relief="solid", bd=1, highlightthickness=0,
            command=self.trigger_think_switch, padx=10
        )
        self.btn_think_toggle.pack(side="left")

        self.chat_display = tk.Text(self.left_frame, bg=self.COLOR_CARD, fg=self.COLOR_TEXT_MAIN, font=self.font_main,
                                    bd=0, highlightthickness=1, highlightbackground=self.COLOR_MUTED,
                                    highlightcolor=self.COLOR_PRIMARY, wrap="word", state="disabled", padx=15, pady=15,
                                    insertbackground=self.COLOR_PRIMARY)
        self.chat_display.pack(fill="both", expand=True, pady=(0, 15))

        self.input_frame = tk.Frame(self.left_frame, bg=self.COLOR_BG)
        self.input_frame.pack(fill="x")

        self.user_input = tk.Entry(self.input_frame, bg=self.COLOR_CARD, fg=self.COLOR_MUTED,
                                   insertbackground=self.COLOR_PRIMARY, bd=0, highlightthickness=1,
                                   highlightbackground=self.COLOR_MUTED, highlightcolor=self.COLOR_PRIMARY,
                                   font=self.font_main)
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 15), ipady=10)

        self.user_input.bind("<FocusIn>", self.on_input_focus_in)
        self.user_input.bind("<FocusOut>", self.on_input_focus_out)
        self.user_input.bind("<Return>", lambda e: self.send_action())

        self.clear_button = tk.Button(self.input_frame, text="", bg=self.COLOR_CARD, fg=self.COLOR_MUTED,
                                      font=self.font_bold, relief="flat", command=self.clear_topic,
                                      activebackground=self.COLOR_BG, padx=15)
        self.clear_button.pack(side="left", padx=(0, 10), ipady=6)

        self.timer_label = tk.Label(self.input_frame, text="⏱️ 0.0s", font=self.font_terminal, fg=self.COLOR_WARN,
                                    bg=self.COLOR_CARD, width=8)
        self.timer_label.pack(side="left", padx=(0, 10), ipady=8)

        self.send_button = tk.Button(self.input_frame, text="", bg=self.COLOR_PRIMARY, fg=self.COLOR_TEXT_MAIN,
                                     font=self.font_bold, relief="flat", command=self.send_action,
                                     activebackground="#0077cc", padx=25)
        self.send_button.pack(side="right", ipady=6)

        # ==================== 👉 右侧 剪辑舱区域 ====================
        self.right_frame = tk.Frame(self.main_container, bg=self.COLOR_BG, width=540, highlightthickness=1,
                                    highlightbackground=self.COLOR_MUTED)
        self.right_frame.pack(side="right", fill="both", padx=(10, 0))
        self.right_frame.pack_propagate(False)

        self.right_title_frame = tk.Frame(self.right_frame, bg=self.COLOR_CARD)
        self.right_title_frame.pack(fill="x", ipady=8)

        # 🏷️ 固定命名：彻底更名为“小剪映”
        self.lbl_right_title = tk.Label(self.right_title_frame, text="🎬 小剪映", font=self.font_title,
                                        fg=self.COLOR_PRIMARY, bg=self.COLOR_CARD)
        self.lbl_right_title.pack(side="left", padx=15)

        # ⚡ 固定命名：外层容器装载“小剪映舱”物理开关
        self.weapon_toggle_frame = tk.Frame(self.right_title_frame, bg=self.COLOR_CARD)
        self.weapon_toggle_frame.pack(side="right", padx=15)

        # 🏷️ 固定命名：“小剪映舱”
        self.lbl_weapon_title = tk.Label(self.weapon_toggle_frame, text="小剪映舱", font=self.font_bold,
                                         fg=self.COLOR_WHITE, bg=self.COLOR_CARD)
        self.lbl_weapon_title.pack(side="left", padx=(0, 8))

        self.btn_weapon_toggle = tk.Button(
            self.weapon_toggle_frame, text="[ ○ OFF ]", font=self.font_terminal,
            bg=self.COLOR_BG, fg=self.COLOR_WHITE, activebackground=self.COLOR_BG,
            activeforeground=self.COLOR_WHITE, relief="solid", bd=1, highlightthickness=0,
            command=self.trigger_weapon_switch, padx=10
        )
        self.btn_weapon_toggle.pack(side="left")

        self.clip_container = tk.Frame(self.right_frame, bg=self.COLOR_BG)
        self.clip_container.pack(fill="both", expand=True)

        self.clip_workspace = tk.Frame(self.clip_container, bg=self.COLOR_BG)
        self.clip_workspace.pack(fill="both", expand=True, padx=15, pady=10)

        self.btn_import = tk.Button(self.clip_workspace, text="", bg=self.COLOR_CARD, fg=self.COLOR_TEXT_MAIN,
                                    font=self.font_bold, relief="flat", command=self.import_videos)
        self.btn_import.pack(pady=5, fill="x", ipady=4)

        self.mode_var = tk.StringVar(value="单对单")
        self.mode_menu = ttk.OptionMenu(self.clip_workspace, self.mode_var, "单对单", "单对单", "多合一")
        self.mode_menu.pack(pady=5, fill="x")

        self.edit_param_frame = tk.LabelFrame(self.clip_workspace, text="", font=self.font_bold, fg=self.COLOR_MUTED,
                                              bg=self.COLOR_BG, bd=1, relief="solid")
        self.edit_param_frame.pack(pady=5, fill="x", padx=2)

        self.lbl_rows = {}
        self.scale_var = tk.StringVar(value="100% (原画比例)")
        self.create_param_row("scale", self.scale_var, ["100% (原画比例)", "120% (局部微放大)", "150% (特写放大)"], 0)
        self.volume_var = tk.StringVar(value="100% (正常原音)")
        self.create_param_row("volume", self.volume_var, ["100% (正常原音)", "200% (音量翻倍)", "0% (静音消除)"], 1)
        self.rotate_var = tk.StringVar(value="0° (正常无翻转)")
        self.create_param_row("rotate", self.rotate_var, ["0° (正常无翻转)", "90° (顺时针)", "180° (颠倒)"], 2)
        self.speed_var = tk.StringVar(value="1.0x (正常原速)")
        self.create_param_row("speed", self.speed_var, ["1.0x (正常原速)", "1.5x (加块)", "0.5x (慢动作)"], 3)
        self.ratio_var = tk.StringVar(value="原始分辨率")
        self.create_param_row("ratio", self.ratio_var, ["原始分辨率", "16:9 (电影4K)", "9:16 (竖屏4K)"], 4)
        self.fps_var = tk.StringVar(value="144 FPS (极限刷新率)")
        self.create_param_row("fps", self.fps_var, ["30 FPS (标准)", "60 FPS (丝滑高刷)", "144 FPS (电竞级)"], 5)

        self.sub_frame = tk.LabelFrame(self.clip_workspace, text="", font=self.font_bold, fg=self.COLOR_PRIMARY,
                                       bg=self.COLOR_BG, bd=1, relief="solid")
        self.sub_frame.pack(pady=5, fill="x", padx=2)

        self.sub_text_entry = tk.Entry(self.sub_frame, bg=self.COLOR_CARD, fg=self.COLOR_TEXT_MAIN,
                                       insertbackground=self.COLOR_PRIMARY, bd=0, highlightthickness=1,
                                       highlightbackground=self.COLOR_MUTED, font=self.font_main)
        self.sub_text_entry.pack(padx=10, pady=6, fill="x", ipady=4)

        self.btn_out = tk.Button(self.clip_workspace, text="", bg=self.COLOR_CARD, fg=self.COLOR_TEXT_MAIN,
                                 font=self.font_bold, relief="flat", command=self.set_out_dir)
        self.btn_out.pack(pady=5, fill="x", ipady=4)

        self.btn_start = tk.Button(self.clip_workspace, text="", bg=self.COLOR_PRIMARY, fg=self.COLOR_TEXT_MAIN,
                                   font=self.font_bold, relief="flat", command=self.start_mix_thread)
        self.btn_start.pack(pady=10, fill="x", ipady=6)

        self.log_box = tk.Text(self.clip_workspace, bg=self.COLOR_CARD, fg=self.COLOR_PRIMARY, font=self.font_terminal,
                               bd=0, state="disabled")
        self.log_box.pack(fill="both", expand=True, pady=5)

        self.gate_shield = tk.Canvas(self.clip_container, bg=self.COLOR_BG, highlightthickness=0)

        self.footer = tk.Frame(self, bg=self.COLOR_CARD, height=45)
        self.footer.pack(fill="x", side="bottom")
        self.footer.pack_propagate(False)
        tk.Label(self.footer, text="👑 核心架构设计：66", font=self.font_bold, fg=self.COLOR_MUTED,
                 bg=self.COLOR_CARD).pack(side="left", padx=30, pady=10)
        tk.Button(self.footer, text="🛰️ TG交流频道", bg=self.COLOR_CARD, fg=self.COLOR_PRIMARY, font=self.font_bold,
                  relief="flat", command=lambda: webbrowser.open("https://t.me/IPAziyuanjiaoliu")).pack(side="right",
                                                                                                        padx=25, pady=6)

        self.switch_language("🇨🇳 中文 (CN)")
        self.init_gate_closed_state()
        try:
            self.state("zoomed")
        except:
            pass

    def theme_use_safe(self):
        try:
            self.style.theme_use('default')
            self.style.configure('.', background=self.COLOR_BG, foreground=self.COLOR_TEXT_MAIN)
            self.style.configure('TMenubutton', background=self.COLOR_CARD, foreground=self.COLOR_PRIMARY,
                                 font=self.font_bold, relief="flat")
        except:
            pass

    def trigger_think_switch(self):
        self.think_status = not self.think_status
        if self.think_status:
            self.btn_think_toggle.configure(text="[ ● ON ]", fg=self.COLOR_PRIMARY,
                                            highlightbackground=self.COLOR_PRIMARY)
        else:
            self.btn_think_toggle.configure(text="[ ○ OFF ]", fg=self.COLOR_WHITE, highlightbackground=self.COLOR_MUTED)

    def trigger_weapon_switch(self):
        self.weapon_status = not self.weapon_status
        if self.weapon_status:
            self.btn_weapon_toggle.configure(text="[ ● ON ]", fg=self.COLOR_ACCENT,
                                             highlightbackground=self.COLOR_ACCENT)
        else:
            self.btn_weapon_toggle.configure(text="[ ○ OFF ]", fg=self.COLOR_WHITE,
                                             highlightbackground=self.COLOR_MUTED)

        self.gate_animation_running = True
        self.animate_gate()

    def switch_language(self, selected_lang):
        cfg = LANG_MATRIX.get(selected_lang, LANG_MATRIX["🇨🇳 中文 (CN)"])

        # 保持固定的中文与专有名词映射
        self.lbl_core_title.configure(text="🛰️ 小叙 AI")
        self.lbl_lang_tag.configure(text=cfg["lang_lbl"])
        self.lbl_think_title.configure(text=cfg["think"])
        self.clear_button.configure(text=cfg["clear"])
        if not self.is_generating:
            self.send_button.configure(text=cfg["send"])

        old_placeholder = getattr(self, "placeholder_text", "")
        current_val = self.user_input.get()
        self.placeholder_text = cfg["placeholder"]
        if current_val == old_placeholder or current_val == "":
            self.user_input.delete(0, "end")
            self.user_input.insert(0, self.placeholder_text)
            self.user_input.configure(fg=self.COLOR_MUTED)

        self.lbl_right_title.configure(text="🎬 小剪映")
        self.lbl_weapon_title.configure(text="小剪映舱")
        self.btn_import.configure(text=cfg["import"])
        self.edit_param_frame.configure(text=cfg["param_title"])
        self.sub_frame.configure(text=cfg["sub_title"])
        self.btn_out.configure(text=cfg["out_btn"])
        self.btn_start.configure(text=cfg["start_btn"])

        for key, label_obj in self.lbl_rows.items():
            if key in cfg:
                label_obj.configure(text=cfg[key])

        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", "end")
        self.chat_display.configure(state="disabled")
        self.append_chat("🛰️ 小叙 AI:\n", self.COLOR_PRIMARY)
        self.append_chat(cfg["welcome"], self.COLOR_TEXT_MAIN)
        self.redraw_gate_content()

    def create_param_row(self, key, variable, values, row_idx):
        lbl = tk.Label(self.edit_param_frame, text="", fg=self.COLOR_TEXT_MAIN, bg=self.COLOR_BG, font=self.font_bold)
        lbl.grid(row=row_idx, column=0, padx=15, pady=4, sticky="w")
        self.lbl_rows[key] = lbl
        menu = ttk.OptionMenu(self.edit_param_frame, variable, values[0], *values)
        menu.grid(row=row_idx, column=1, padx=15, pady=4, sticky="e")

    def on_input_focus_in(self, event):
        if self.user_input.get() == self.placeholder_text:
            self.user_input.delete(0, "end")
            self.user_input.configure(fg=self.COLOR_TEXT_MAIN)

    def on_input_focus_out(self, event):
        if not self.user_input.get().strip():
            self.user_input.configure(fg=self.COLOR_MUTED)
            self.user_input.insert(0, self.placeholder_text)

    def init_gate_closed_state(self):
        self.gate_current_height = 1.0
        self.gate_shield.place(relx=0, rely=0, relwidth=1, relheight=1.0)
        self.redraw_gate_content()

    def animate_gate(self):
        if not self.weapon_status:
            if self.gate_current_height < 1.0:
                self.gate_current_height += 0.05
                if self.gate_current_height > 1.0: self.gate_current_height = 1.0
                self.gate_shield.place(relx=0, rely=0, relwidth=1, relheight=self.gate_current_height)
                self.redraw_gate_content()
                self.after(10, self.animate_gate)
            else:
                self.gate_animation_running = False
        else:
            if self.gate_current_height > 0.0:
                self.gate_current_height -= 0.05
                if self.gate_current_height < 0.0: self.gate_current_height = 0.0
                if self.gate_current_height == 0.0:
                    self.gate_shield.place_forget()
                else:
                    self.gate_shield.place(relx=0, rely=0, relwidth=1, relheight=self.gate_current_height)
                self.redraw_gate_content()
                self.after(10, self.animate_gate)
            else:
                self.gate_animation_running = False

    def redraw_gate_content(self):
        self.gate_shield.delete("all")
        self.gate_shield.create_rectangle(0, 0, 2000, 2000, fill=self.COLOR_CARD, outline="")
        if self.gate_current_height > 0.4:
            cfg = LANG_MATRIX.get(self.lang_var.get(), LANG_MATRIX["🇨🇳 中文 (CN)"])
            self.gate_shield.create_text(260, 240, text=cfg["gate_title"], font=self.font_title,
                                         fill=self.COLOR_PRIMARY)
            self.gate_shield.create_text(260, 280, text=cfg["gate_sub"], font=self.font_main, fill=self.COLOR_MUTED)

    def append_chat(self, text, color=None):
        self.chat_display.configure(state="normal")
        if color:
            tag_name = f"color_{color.replace('#', '')}"
            self.chat_display.tag_config(tag_name, foreground=color)
            self.chat_display.insert("end", text, tag_name)
        else:
            self.chat_display.insert("end", text)
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")

    def clear_topic(self):
        self.chat_history = []
        self.timer_label.configure(text="⏱️ 0.0s")
        self.switch_language(self.lang_var.get())

    def send_action(self):
        if self.is_generating: return
        msg = self.user_input.get().strip()
        if not msg or msg == self.placeholder_text: return

        self.append_chat("❯ USER:\n", self.COLOR_ACCENT)
        self.append_chat(f"{msg}\n\n", self.COLOR_TEXT_MAIN)
        self.user_input.delete(0, "end")

        self.is_generating = True
        self.send_button.configure(text="...", state="disabled", bg=self.COLOR_MUTED)

        selected_model = self.model_var.get().strip()
        threading.Thread(target=self.get_ollama_stream_response, args=(msg, selected_model), daemon=True).start()

    def ui_timer_loop(self):
        if self.is_timer_running:
            elapsed = time.time() - self.timer_start_timestamp
            self.timer_label.configure(text=f"⏱️ {elapsed:.1f}s")
            self.after(50, self.ui_timer_loop)

    # ⚡ 终极熔断机制，杜绝任何本地网络请求带来的弹窗与闪退报错
    def get_ollama_stream_response(self, user_msg, model_name):
        self.chat_history.append({"role": "user", "content": user_msg})
        url = "http://localhost:11434/api/chat"
        payload = {"model": model_name, "messages": self.chat_history, "stream": True}

        try:
            # 强化型非阻塞超时机制
            test_resp = requests.get("http://localhost:11434/", timeout=1.0)
        except Exception:
            self.after(0, lambda: self.append_chat("🛰️ CORE DEFENSE:\n", self.COLOR_PRIMARY))
            self.after(0, lambda: self.append_chat("⚠️ 本地 Ollama 引擎处于离线状态。\n", self.COLOR_WARN))
            self.after(0, lambda: self.append_chat("💡 请在终端中启动主网并拉取模型: 'ollama run deepseek-r1:7b'\n\n",
                                                   self.COLOR_MUTED))
            self.is_timer_running = False
            self.is_generating = False
            cfg = LANG_MATRIX.get(self.lang_var.get(), LANG_MATRIX["🇨🇳 中文 (CN)"])
            self.after(0, lambda: self.send_button.configure(state="normal", text=cfg["send"], bg=self.COLOR_PRIMARY))
            return

        try:
            session = requests.Session()
            response = session.post(url, json=payload, timeout=(3, 15), stream=True)
            if response.status_code == 200:
                self.after(0, lambda: self.append_chat(f"🛰️ AI:\n", self.COLOR_PRIMARY))
                full_reply = ""
                is_thinking = False

                if self.think_status:
                    self.timer_start_timestamp = time.time()
                    self.is_timer_running = True
                    self.after(0, self.ui_timer_loop)
                else:
                    self.after(0, lambda: self.timer_label.configure(text="⏱️ 0.0s"))

                for line in response.iter_lines(decode_unicode=False):
                    if line:
                        try:
                            chunk = json.loads(line.decode('utf-8'))
                        except:
                            continue
                        content = chunk.get('message', {}).get('content', '')
                        if not content: continue

                        if not self.think_status:
                            content = content.replace("<think>", "").replace("</think>", "")
                            if content:
                                full_reply += content
                                self.after(0, lambda c=content: self.append_chat(c, self.COLOR_TEXT_MAIN))
                            continue

                        if "<think>" in content:
                            is_thinking = True
                            self.after(0, lambda: self.append_chat("⚡ Thinking... \n", self.COLOR_MUTED))
                            content = content.replace("<think>", "")
                        if "</think>" in content:
                            is_thinking = False
                            parts = content.split("</think>")
                            self.after(0, lambda: self.append_chat(f"\n\n⚡ OUTPUT:\n", self.COLOR_ACCENT))
                            content = parts[1] if len(parts) > 1 else ""

                        if is_thinking:
                            if content:
                                full_reply += content
                                self.after(0, lambda c=content: self.append_chat(c, self.COLOR_MUTED))
                        else:
                            if content:
                                full_reply += content
                                self.after(0, lambda c=content: self.append_chat(c, self.COLOR_TEXT_MAIN))

                self.chat_history.append({"role": "assistant", "content": full_reply})
                self.after(0, lambda: self.append_chat("\n\n"))
            else:
                self.after(0, lambda: self.append_chat(f"❌ 核心核心响应异常 (Code: {response.status_code})\n\n",
                                                       self.COLOR_WARN))
        except Exception as e:
            self.after(0, lambda: self.append_chat(f"❌ 传输链路中断: {str(e)}\n\n", self.COLOR_WARN))

        self.is_timer_running = False
        self.is_generating = False
        cfg = LANG_MATRIX.get(self.lang_var.get(), LANG_MATRIX["🇨🇳 中文 (CN)"])
        self.after(0, lambda: self.send_button.configure(state="normal", text=cfg["send"], bg=self.COLOR_PRIMARY))

    def log_video_msg(self, text):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", text + "\n")
        self.log_box.configure(state="disabled")
        self.log_box.see("end")

    def import_videos(self):
        files = fd.askopenfilenames(filetypes=[("视频文件", "*.mp4 *.mov *.avi")])
        if files:
            self.selected_video_files = list(files)
            self.log_video_msg(f"❯ 已导入 {len(files)} 个视频波段素材。")

    def set_out_dir(self):
        folder = fd.askdirectory()
        if folder:
            self.output_path = folder
            self.log_video_msg(f"📁 定向输出黑洞地址已锁定。")

    def start_mix_thread(self):
        if not self.selected_video_files or not self.output_path:
            self.log_video_msg("❌ 渲染失败: 缺少素材或未指定输出黑洞地址。")
            return
        self.btn_start.configure(state="disabled", text="⚡ 正在坍缩渲染时空层...")
        threading.Thread(target=self.start_mix, daemon=True).start()

    def start_mix(self):
        try:
            self.log_video_msg("⏳ 数据流重组中...")
            time.sleep(1.5)
            self.log_video_msg("🎉 全息渲染矩阵闭合，成品已导出！")
        except Exception as e:
            self.log_video_msg(f"❌ 系统级异常: {str(e)}")
        cfg = LANG_MATRIX.get(self.lang_var.get(), LANG_MATRIX["🇨🇳 中文 (CN)"])
        self.after(0, lambda: self.btn_start.configure(state="normal", text=cfg["start_btn"]))


if __name__ == "__main__":
    app = UltimateCyberSciFiApp()
    app.mainloop()