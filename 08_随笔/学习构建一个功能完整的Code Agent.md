---
tags:
  - 随笔
  - AI_Agent
创建时间: 2026-02-07T21:00:00
开始日期: 2026-02-07
结束日期:
DeadLine: 2026-02-28
---
# 🚀 **一步一步实现 Code Agent 教程**

让我带你从零开始，一步步构建一个功能完整的 Code Agent。我们将采用**渐进式开发**，确保每一步都能理解并运行。

## 📋 **学习路线图**

```
第1步：环境准备 → 第2步：基础API调用 → 第3步：简单代码生成
    ↓                       ↓                       ↓
第4步：添加代码审查 → 第5步：添加测试生成 → 第6步：创建项目结构
    ↓                       ↓                       ↓
第7步：构建Web界面 → 第8步：添加高级功能 → 第9步：部署上线
```

---

## **第1步：环境准备与配置**

### **1.1 创建项目目录**
```bash
mkdir code-agent-tutorial
cd code-agent-tutorial
```

### **1.2 创建虚拟环境**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **1.3 安装依赖包**
创建 `requirements.txt` 文件：
```txt
flask==2.3.3
requests==2.31.0
python-dotenv==1.0.0
```

安装：
```bash
pip install -r requirements.txt
```

### **1.4 获取 DeepSeek API 密钥**
1. 访问 [DeepSeek平台](https://platform.deepseek.com/)
2. 注册/登录账号
3. 进入API Keys页面
4. 创建新的API密钥并复制

### **1.5 设置环境变量**
创建 `.env` 文件：
```env
DEEPSEEK_API_KEY=你的API密钥
```

创建 `.gitignore` 文件：
```gitignore
venv/
__pycache__/
*.pyc
.env
workspace/
```

---

## **第2步：基础 API 调用模块**

创建 `api_client.py`：
```python
import os
import requests
from typing import Dict, List, Optional
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class DeepSeekAPIClient:
    """DeepSeek API 基础客户端"""
    
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("请在 .env 文件中设置 DEEPSEEK_API_KEY")
        
        self.base_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def chat(self, 
             messages: List[Dict[str, str]], 
             model: str = "deepseek-chat",
             temperature: float = 0.7,
             max_tokens: Optional[int] = None) -> Dict:
        """
        调用聊天API
        
        参数:
            messages: 消息列表，格式 [{"role": "user", "content": "你好"}]
            model: 模型名称
            temperature: 温度参数（0-1）
            max_tokens: 最大token数
        
        返回:
            API响应字典
        """
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature
        }
        
        if max_tokens:
            payload["max_tokens"] = max_tokens
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()  # 检查HTTP错误
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API调用失败: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"响应内容: {e.response.text}")
            raise
    
    def generate_text(self, 
                     prompt: str, 
                     system_prompt: Optional[str] = None) -> str:
        """
        简化版文本生成
        
        参数:
            prompt: 用户输入
            system_prompt: 系统提示词
        
        返回:
            生成的文本
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        response = self.chat(messages)
        
        # 提取返回的文本
        try:
            return response["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            print(f"解析响应失败: {e}")
            print(f"响应内容: {response}")
            raise


# 测试函数
def test_api_client():
    """测试API客户端是否正常工作"""
    try:
        client = DeepSeekAPIClient()
        
        # 简单的测试对话
        test_response = client.generate_text(
            prompt="Hello, please say 'API connection successful' in Chinese.",
            system_prompt="You are a helpful assistant."
        )
        
        print("✅ API连接成功!")
        print(f"测试响应: {test_response}")
        return True
        
    except Exception as e:
        print(f"❌ API连接失败: {e}")
        return False


if __name__ == "__main__":
    # 运行测试
    test_api_client()
```

运行测试：
```bash
python api_client.py
```

你应该看到输出：
```
✅ API连接成功!
测试响应: API连接成功！
```

---

## **第3步：简单代码生成器**

创建 `code_generator.py`：
```python
import re
from api_client import DeepSeekAPIClient
from typing import Dict, List

class SimpleCodeGenerator:
    """简单的代码生成器"""
    
    def __init__(self):
        self.api_client = DeepSeekAPIClient()
        self.conversation_history = []
    
    def generate_python_code(self, requirement: str) -> Dict[str, str]:
        """
        生成Python代码
        
        参数:
            requirement: 需求描述
        
        返回:
            包含代码和解释的字典
        """
        
        system_prompt = """你是一个专业的Python程序员。请根据用户需求生成Python代码。

要求：
1. 生成完整、可运行的代码
2. 包含必要的注释
3. 添加基本的错误处理
4. 代码要简洁高效
5. 在代码后添加## 解释##部分说明代码功能

格式示例：
```python
# 你的代码
print("Hello World")
```
## 解释##
这是一个简单的Hello World程序。"""

        user_prompt = f"请生成Python代码实现：{requirement}"
        
        try:
            response = self.api_client.generate_text(
                prompt=user_prompt,
                system_prompt=system_prompt
            )
            
            # 解析响应，分离代码和解释
            result = self._parse_response(response)
            
            # 保存到对话历史
            self.conversation_history.append({
                "role": "user",
                "content": user_prompt
            })
            self.conversation_history.append({
                "role": "assistant", 
                "content": response
            })
            
            return result
            
        except Exception as e:
            return {
                "error": f"生成代码失败: {str(e)}",
                "code": "",
                "explanation": ""
            }
    
    def _parse_response(self, response: str) -> Dict[str, str]:
        """解析AI响应，提取代码和解释"""
        
        # 查找代码块
        code_pattern = r'```python\s*(.*?)\s*```'
        code_match = re.search(code_pattern, response, re.DOTALL)
        
        code = code_match.group(1) if code_match else ""
        
        # 查找解释部分
        explanation_pattern = r'##\s*解释\s*##\s*(.*)'
        explanation_match = re.search(explanation_pattern, response, re.DOTALL)
        
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        
        # 如果没有找到解释，使用响应内容
        if not explanation:
            explanation = response
        
        return {
            "code": code.strip(),
            "explanation": explanation.strip(),
            "raw_response": response
        }
    
    def get_history(self) -> List[Dict]:
        """获取对话历史"""
        return self.conversation_history
    
    def clear_history(self):
        """清空对话历史"""
        self.conversation_history = []


# 测试函数
def test_code_generator():
    """测试代码生成器"""
    print("🧪 测试代码生成器...")
    
    generator = SimpleCodeGenerator()
    
    # 测试1: 简单需求
    print("\n1. 测试简单需求：计算两个数的和")
    result = generator.generate_python_code("计算两个数的和")
    
    print("生成的代码：")
    print("-" * 40)
    print(result["code"])
    print("-" * 40)
    print(f"解释：\n{result['explanation']}")
    
    # 测试2: 稍微复杂的需求
    print("\n2. 测试复杂需求：读取CSV文件并计算平均值")
    result2 = generator.generate_python_code("读取CSV文件并计算数值列的平均值")
    
    if result2.get("code"):
        print("✅ 代码生成成功！")
        print(f"代码长度：{len(result2['code'])} 字符")
    
    # 显示历史记录
    print(f"\n对话历史记录数：{len(generator.get_history())}")
    
    return generator


if __name__ == "__main__":
    generator = test_code_generator()
    
    # 交互式测试
    print("\n🎮 交互式测试（输入 'quit' 退出）")
    
    while True:
        user_input = input("\n请输入代码需求：")
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        if user_input.strip():
            result = generator.generate_python_code(user_input)
            
            if result.get("code"):
                print("\n" + "="*50)
                print("生成的代码：")
                print("="*50)
                print(result["code"])
                print("="*50)
                
                # 可选：保存到文件
                save = input("\n是否保存到文件？(y/n): ")
                if save.lower() == 'y':
                    filename = input("输入文件名（例如：my_code.py）: ")
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(result["code"])
                    print(f"✅ 代码已保存到 {filename}")
            else:
                print(f"❌ 生成失败: {result.get('error', '未知错误')}")
```

运行测试：
```bash
python code_generator.py
```

测试成功后，尝试输入一些代码需求，比如：
- "生成一个斐波那契数列函数"
- "创建一个简单的爬虫获取网页标题"
- "写一个计算器类，支持加减乘除"

---

## **第4步：添加代码审查功能**

创建 `code_reviewer.py`：
```python
import ast
from api_client import DeepSeekAPIClient
from typing import Dict, List, Tuple

class CodeReviewer:
    """代码审查器"""
    
    def __init__(self):
        self.api_client = DeepSeekAPIClient()
    
    def review_code(self, code: str, language: str = "python") -> Dict:
        """
        审查代码
        
        参数:
            code: 要审查的代码
            language: 编程语言
        
        返回:
            审查结果
        """
        
        system_prompt = f"""你是一个资深的{language}代码审查专家。请仔细审查以下代码：

审查要点：
1. 代码质量和可读性
2. 性能优化建议
3. 潜在的错误和边界情况
4. 安全漏洞检查
5. 是否符合最佳实践
6. 改进建议

请按以下格式返回：
## 代码质量评分## (1-10分)
## 主要问题## 
1. 问题1
2. 问题2
## 改进建议## 
1. 建议1
2. 建议2
## 安全评估## 
## 性能建议## """

        user_prompt = f"请审查以下{language}代码：\n```{language}\n{code}\n```"
        
        try:
            response = self.api_client.generate_text(
                prompt=user_prompt,
                system_prompt=system_prompt
            )
            
            # 分析代码复杂度
            complexity = self._analyze_code_complexity(code) if language == "python" else {}
            
            # 解析响应
            review_data = self._parse_review_response(response)
            
            return {
                "success": True,
                "review": review_data,
                "complexity_analysis": complexity,
                "raw_response": response
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "review": {},
                "complexity_analysis": {}
            }
    
    def _analyze_code_complexity(self, code: str) -> Dict:
        """分析Python代码复杂度"""
        try:
            tree = ast.parse(code)
            
            # 统计各种元素
            functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
            imports = [node for node in ast.walk(tree) if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)]
            
            # 计算行数
            lines = code.strip().split('\n')
            code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
            
            # 计算圈复杂度（简化版）
            complexity_score = len(functions) * 2 + len(classes) * 3
            
            return {
                "function_count": len(functions),
                "class_count": len(classes),
                "import_count": len(imports),
                "total_lines": len(lines),
                "code_lines": len(code_lines),
                "comment_lines": len(lines) - len(code_lines),
                "complexity_score": complexity_score,
                "complexity_level": self._get_complexity_level(complexity_score)
            }
            
        except SyntaxError as e:
            return {
                "error": f"语法错误: {str(e)}",
                "complexity_score": 0,
                "complexity_level": "无法分析"
            }
    
    def _get_complexity_level(self, score: int) -> str:
        """根据分数获取复杂度等级"""
        if score < 5:
            return "简单"
        elif score < 10:
            return "中等"
        elif score < 20:
            return "复杂"
        else:
            return "非常复杂"
    
    def _parse_review_response(self, response: str) -> Dict:
        """解析审查响应"""
        patterns = {
            "quality_score": r'##\s*代码质量评分##\s*([\d\.]+)',
            "main_issues": r'##\s*主要问题##\s*(.*?)(?=##|$)',
            "suggestions": r'##\s*改进建议##\s*(.*?)(?=##|$)',
            "security": r'##\s*安全评估##\s*(.*?)(?=##|$)',
            "performance": r'##\s*性能建议##\s*(.*?)(?=##|$)'
        }
        
        result = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, response, re.DOTALL | re.IGNORECASE)
            if match:
                result[key] = match.group(1).strip()
            else:
                result[key] = ""
        
        return result


# 测试函数
def test_code_reviewer():
    """测试代码审查器"""
    print("🧪 测试代码审查器...")
    
    reviewer = CodeReviewer()
    
    # 测试代码
    test_code = """
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
"""
    
    print("审查的代码：")
    print("-" * 40)
    print(test_code)
    print("-" * 40)
    
    # 进行审查
    result = reviewer.review_code(test_code)
    
    if result["success"]:
        review = result["review"]
        complexity = result["complexity_analysis"]
        
        print("\n✅ 审查结果：")
        print(f"代码质量评分：{review.get('quality_score', 'N/A')}")
        
        if review.get("main_issues"):
            print("\n主要问题：")
            print(review["main_issues"])
        
        if review.get("suggestions"):
            print("\n改进建议：")
            print(review["suggestions"])
        
        print(f"\n复杂度分析：")
        print(f"- 函数数量：{complexity.get('function_count', 0)}")
        print(f"- 总行数：{complexity.get('total_lines', 0)}")
        print(f"- 代码行数：{complexity.get('code_lines', 0)}")
        print(f"- 复杂度等级：{complexity.get('complexity_level', 'N/A')}")
    
    return reviewer


if __name__ == "__main__":
    reviewer = test_code_reviewer()
    
    # 交互式测试
    print("\n🎮 交互式代码审查（输入 'quit' 退出）")
    
    while True:
        print("\n1. 输入代码")
        print("2. 从文件读取")
        print("3. 退出")
        
        choice = input("\n请选择 (1/2/3): ")
        
        if choice == "3":
            break
        elif choice == "1":
            print("\n请输入代码（输入 'END' 结束）：")
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)
            code = "\n".join(lines)
        elif choice == "2":
            filename = input("输入文件名: ")
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    code = f.read()
                print(f"✅ 从 {filename} 读取成功")
            except FileNotFoundError:
                print(f"❌ 文件 {filename} 不存在")
                continue
        else:
            print("❌ 无效选择")
            continue
        
        if code.strip():
            result = reviewer.review_code(code)
            
            if result["success"]:
                review = result["review"]
                print("\n" + "="*60)
                print("代码审查报告")
                print("="*60)
                
                for key, value in review.items():
                    if value:
                        print(f"\n{key.replace('_', ' ').title()}:")
                        print(value)
                
                print("\n" + "="*60)
            else:
                print(f"❌ 审查失败: {result.get('error')}")
```

运行测试：
```bash
python code_reviewer.py
```

---

## **第5步：整合代码生成与审查**

创建 `code_agent.py`：
```python
import os
import json
from datetime import datetime
from code_generator import SimpleCodeGenerator
from code_reviewer import CodeReviewer

class CodeAgent:
    """完整的Code Agent"""
    
    def __init__(self):
        self.generator = SimpleCodeGenerator()
        self.reviewer = CodeReviewer()
        self.workspace_dir = "workspace"
        
        # 创建工作空间目录
        os.makedirs(self.workspace_dir, exist_ok=True)
    
    def generate_and_review(self, requirement: str, language: str = "python") -> Dict:
        """
        生成代码并进行审查
        
        参数:
            requirement: 需求描述
            language: 编程语言
        
        返回:
            完整的结果
        """
        print(f"🚀 开始处理需求: {requirement}")
        
        # 1. 生成代码
        print("📝 生成代码中...")
        gen_result = self.generator.generate_python_code(requirement)
        
        if gen_result.get("error"):
            return {
                "success": False,
                "error": f"代码生成失败: {gen_result['error']}",
                "stage": "generation"
            }
        
        # 2. 审查代码
        print("🔍 审查代码中...")
        review_result = self.reviewer.review_code(gen_result["code"], language)
        
        # 3. 保存结果
        print("💾 保存结果中...")
        save_result = self._save_results(requirement, gen_result, review_result)
        
        return {
            "success": True,
            "generation": gen_result,
            "review": review_result if review_result["success"] else None,
            "files": save_result
        }
    
    def _save_results(self, requirement: str, gen_result: Dict, review_result: Dict) -> Dict:
        """保存生成的结果"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        project_id = f"project_{timestamp}"
        project_dir = os.path.join(self.workspace_dir, project_id)
        
        os.makedirs(project_dir, exist_ok=True)
        
        files_created = []
        
        # 1. 保存生成的代码
        if gen_result.get("code"):
            code_file = os.path.join(project_dir, "generated_code.py")
            with open(code_file, 'w', encoding='utf-8') as f:
                f.write(gen_result["code"])
            files_created.append(code_file)
        
        # 2. 保存解释
        if gen_result.get("explanation"):
            explain_file = os.path.join(project_dir, "explanation.txt")
            with open(explain_file, 'w', encoding='utf-8') as f:
                f.write(gen_result["explanation"])
            files_created.append(explain_file)
        
        # 3. 保存审查报告
        if review_result.get("success") and review_result.get("review"):
            review_file = os.path.join(project_dir, "code_review.txt")
            
            review_content = "=" * 60 + "\n"
            review_content += "代码审查报告\n"
            review_content += "=" * 60 + "\n\n"
            
            review = review_result["review"]
            for key, value in review.items():
                if value:
                    review_content += f"{key.replace('_', ' ').title()}:\n"
                    review_content += f"{value}\n\n"
            
            if review_result.get("complexity_analysis"):
                complexity = review_result["complexity_analysis"]
                review_content += "复杂度分析:\n"
                for key, value in complexity.items():
                    review_content += f"  {key}: {value}\n"
            
            with open(review_file, 'w', encoding='utf-8') as f:
                f.write(review_content)
            files_created.append(review_file)
        
        # 4. 保存元数据
        metadata = {
            "requirement": requirement,
            "timestamp": timestamp,
            "project_id": project_id,
            "files": [os.path.basename(f) for f in files_created]
        }
        
        meta_file = os.path.join(project_dir, "metadata.json")
        with open(meta_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        files_created.append(meta_file)
        
        return {
            "project_dir": project_dir,
            "files_created": files_created,
            "metadata": metadata
        }
    
    def list_projects(self) -> List[Dict]:
        """列出所有项目"""
        projects = []
        
        if os.path.exists(self.workspace_dir):
            for project_id in os.listdir(self.workspace_dir):
                project_dir = os.path.join(self.workspace_dir, project_id)
                meta_file = os.path.join(project_dir, "metadata.json")
                
                if os.path.exists(meta_file):
                    try:
                        with open(meta_file, 'r', encoding='utf-8') as f:
                            metadata = json.load(f)
                        projects.append(metadata)
                    except:
                        pass
        
        return sorted(projects, key=lambda x: x.get("timestamp", ""), reverse=True)


# 测试函数
def test_code_agent():
    """测试完整的Code Agent"""
    print("🤖 测试Code Agent...")
    
    agent = CodeAgent()
    
    # 测试需求
    test_requirements = [
        "生成一个函数，计算斐波那契数列的第n项",
        "创建一个简单的网页爬虫，获取指定URL的标题",
        "实现一个简单的计算器类，支持加减乘除"
    ]
    
    for i, req in enumerate(test_requirements, 1):
        print(f"\n{'='*60}")
        print(f"测试 {i}: {req}")
        print('='*60)
        
        result = agent.generate_and_review(req)
        
        if result["success"]:
            print("✅ 处理成功！")
            print(f"项目目录: {result['files']['project_dir']}")
            print(f"生成文件数: {len(result['files']['files_created'])}")
            
            if result.get("review"):
                review = result["review"]["review"]
                if review.get("quality_score"):
                    print(f"代码质量评分: {review['quality_score']}")
        else:
            print(f"❌ 处理失败: {result.get('error')}")
    
    # 显示所有项目
    print(f"\n📁 所有项目列表:")
    projects = agent.list_projects()
    for project in projects:
        print(f"- {project['project_id']}: {project['requirement'][:50]}...")


if __name__ == "__main__":
    test_code_agent()
    
    # 交互式模式
    print("\n🎮 交互式模式（输入 'quit' 退出）")
    
    agent = CodeAgent()
    
    while True:
        print("\n选项:")
        print("1. 生成新代码")
        print("2. 查看历史项目")
        print("3. 退出")
        
        choice = input("\n请选择 (1/2/3): ")
        
        if choice == "3":
            break
        elif choice == "1":
            requirement = input("\n请输入代码需求: ")
            if requirement.strip():
                result = agent.generate_and_review(requirement)
                
                if result["success"]:
                    print("\n✅ 任务完成！")
                    print(f"📁 项目目录: {result['files']['project_dir']}")
                    
                    # 询问是否查看文件
                    view = input("\n是否查看生成的文件？(y/n): ")
                    if view.lower() == 'y':
                        project_dir = result['files']['project_dir']
                        for file in os.listdir(project_dir):
                            filepath = os.path.join(project_dir, file)
                            if os.path.isfile(filepath):
                                print(f"\n📄 {file}:")
                                print("-" * 40)
                                try:
                                    with open(filepath, 'r', encoding='utf-8') as f:
                                        content = f.read()
                                        print(content[:500])  # 只显示前500字符
                                        if len(content) > 500:
                                            print("... (内容过长，已截断)")
                                except:
                                    print("(无法读取文件内容)")
                                print("-" * 40)
                else:
                    print(f"\n❌ 失败: {result.get('error')}")
        elif choice == "2":
            projects = agent.list_projects()
            if projects:
                print(f"\n📚 历史项目 ({len(projects)} 个):")
                for i, project in enumerate(projects, 1):
                    print(f"{i}. {project['project_id']}")
                    print(f"   需求: {project['requirement'][:80]}...")
            else:
                print("\n📭 暂无历史项目")
```

运行测试：
```bash
python code_agent.py
```

---

## **第6步：创建Web界面**

创建 `web_app.py`：
```python
from flask import Flask, render_template, request, jsonify, send_file
import os
import zipfile
from code_agent import CodeAgent
from datetime import datetime

app = Flask(__name__)
agent = CodeAgent()

# 存储临时数据的目录
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    """主页"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_code():
    """生成代码API"""
    try:
        data = request.json
        requirement = data.get('requirement', '').strip()
        language = data.get('language', 'python')
        
        if not requirement:
            return jsonify({
                "success": False,
                "error": "请提供需求描述"
            }), 400
        
        # 调用Code Agent生成代码
        result = agent.generate_and_review(requirement, language)
        
        if result["success"]:
            return jsonify({
                "success": True,
                "project_id": result["files"]["metadata"]["project_id"],
                "files": result["files"]["files_created"],
                "review": result["review"],
                "generation": result["generation"]
            })
        else:
            return jsonify({
                "success": False,
                "error": result.get("error", "生成失败")
            }), 500
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"服务器错误: {str(e)}"
        }), 500

@app.route('/projects', methods=['GET'])
def list_projects():
    """列出所有项目"""
    projects = agent.list_projects()
    return jsonify({
        "success": True,
        "projects": projects
    })

@app.route('/project/<project_id>', methods=['GET'])
def get_project(project_id):
    """获取项目详情"""
    project_dir = os.path.join(agent.workspace_dir, project_id)
    
    if not os.path.exists(project_dir):
        return jsonify({
            "success": False,
            "error": "项目不存在"
        }), 404
    
    # 读取项目文件
    files = []
    for filename in os.listdir(project_dir):
        filepath = os.path.join(project_dir, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                files.append({
                    "name": filename,
                    "content": content,
                    "size": len(content)
                })
            except:
                files.append({
                    "name": filename,
                    "error": "无法读取文件",
                    "size": 0
                })
    
    return jsonify({
        "success": True,
        "project_id": project_id,
        "files": files
    })

@app.route('/download/<project_id>', methods=['GET'])
def download_project(project_id):
    """下载项目为ZIP文件"""
    project_dir = os.path.join(agent.workspace_dir, project_id)
    
    if not os.path.exists(project_dir):
        return "项目不存在", 404
    
    # 创建ZIP文件
    zip_filename = f"{project_id}.zip"
    zip_path = os.path.join(UPLOAD_FOLDER, zip_filename)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, project_dir)
                zipf.write(file_path, arcname)
    
    return send_file(zip_path, as_attachment=True, download_name=zip_filename)

# 创建HTML模板
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 Code Agent - AI编程助手</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            color: white;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .main-content {
            display: flex;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        @media (max-width: 768px) {
            .main-content {
                flex-direction: column;
            }
        }
        
        .generator-panel, .results-panel {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        .generator-panel {
            flex: 1;
        }
        
        .results-panel {
            flex: 2;
            display: none;
        }
        
        .panel-title {
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: #333;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .panel-title i {
            color: #667eea;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }
        
        textarea, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        
        textarea {
            min-height: 150px;
            resize: vertical;
            font-family: monospace;
        }
        
        textarea:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            display: flex;
            align-items: center;
            gap: 10px;
            justify-content: center;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        
        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        
        .loading i {
            font-size: 2rem;
            color: #667eea;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            100% { transform: rotate(360deg); }
        }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 10px;
        }
        
        .tab {
            padding: 10px 20px;
            border: none;
            background: none;
            font-size: 16px;
            cursor: pointer;
            border-radius: 6px;
            transition: all 0.3s;
        }
        
        .tab.active {
            background: #667eea;
            color: white;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .code-display {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.5;
        }
        
        .review-section {
            background: #f0f7ff;
            border-radius: 8px;
            padding: 20px;
            margin-top: 20px;
        }
        
        .score-badge {
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        
        .issues-list, .suggestions-list {
            list-style-type: none;
        }
        
        .issues-list li, .suggestions-list li {
            padding: 10px;
            margin-bottom: 10px;
            background: white;
            border-radius: 6px;
            border-left: 4px solid #ff6b6b;
        }
        
        .suggestions-list li {
            border-left-color: #4CAF50;
        }
        
        .file-list {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }
        
        .file-item {
            background: #f0f0f0;
            padding: 10px 15px;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .file-item:hover {
            background: #e0e0e0;
        }
        
        .file-item.active {
            background: #667eea;
            color: white;
        }
        
        .actions {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        
        .secondary-btn {
            background: #6c757d;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }
        
        .projects-list {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        .project-item {
            padding: 15px;
            border-bottom: 1px solid #eee;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .project-item:hover {
            background: #f8f9fa;
        }
        
        .project-item:last-child {
            border-bottom: none;
        }
        
        .project-title {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .project-description {
            color: #666;
            font-size: 14px;
        }
        
        .project-meta {
            display: flex;
            gap: 15px;
            font-size: 12px;
            color: #999;
            margin-top: 5px;
        }
        
        .error-message {
            background: #ffebee;
            color: #c62828;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .success-message {
            background: #e8f5e9;
            color: #2e7d32;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-robot"></i> Code Agent</h1>
            <p>AI驱动的智能代码生成与审查助手</p>
        </div>
        
        <div class="main-content">
            <div class="generator-panel">
                <h2 class="panel-title"><i class="fas fa-code"></i> 代码生成</h2>
                
                <div id="errorMessage" class="error-message" style="display: none;"></div>
                <div id="successMessage" class="success-message" style="display: none;"></div>
                
                <div class="form-group">
                    <label for="requirement"><i class="fas fa-edit"></i> 描述你的需求</label>
                    <textarea id="requirement" placeholder="例如：创建一个Python函数，计算斐波那契数列的第n项..."></textarea>
                </div>
                
                <div class="form-group">
                    <label for="language"><i class="fas fa-language"></i> 选择编程语言</label>
                    <select id="language">
                        <option value="python">Python</option>
                        <option value="javascript">JavaScript</option>
                        <option value="java">Java</option>
                        <option value="cpp">C++</option>
                        <option value="html">HTML/CSS</option>
                    </select>
                </div>
                
                <button id="generateBtn" class="btn">
                    <i class="fas fa-magic"></i> 生成代码
                </button>
                
                <div id="loading" class="loading">
                    <i class="fas fa-spinner"></i>
                    <p>AI正在思考中，请稍候...</p>
                </div>
            </div>
            
            <div id="resultsPanel" class="results-panel">
                <h2 class="panel-title"><i class="fas fa-file-code"></i> 生成结果</h2>
                
                <div class="file-list" id="fileList"></div>
                
                <div class="tabs">
                    <button class="tab active" onclick="switchTab('codeTab')">代码</button>
                    <button class="tab" onclick="switchTab('reviewTab')">审查报告</button>
                    <button class="tab" onclick="switchTab('explanationTab')">解释</button>
                </div>
                
                <div id="codeTab" class="tab-content active">
                    <div class="code-display" id="codeDisplay"></div>
                </div>
                
                <div id="reviewTab" class="tab-content">
                    <div id="reviewDisplay"></div>
                </div>
                
                <div id="explanationTab" class="tab-content">
                    <div id="explanationDisplay"></div>
                </div>
                
                <div class="actions">
                    <button id="downloadBtn" class="btn secondary-btn">
                        <i class="fas fa-download"></i> 下载项目
                    </button>
                    <button id="newProjectBtn" class="btn secondary-btn">
                        <i class="fas fa-plus"></i> 新建项目
                    </button>
                </div>
            </div>
        </div>
        
        <div class="projects-list">
            <h2 class="panel-title"><i class="fas fa-history"></i> 历史项目</h2>
            <div id="projectsList"></div>
        </div>
    </div>

    <script>
        let currentProjectId = null;
        
        // 初始化加载项目列表
        window.onload = loadProjects;
        
        function loadProjects() {
            fetch('/projects')
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        const projectsList = document.getElementById('projectsList');
                        projectsList.innerHTML = '';
                        
                        if (data.projects.length === 0) {
                            projectsList.innerHTML = '<p style="text-align: center; color: #999;">暂无项目</p>';
                            return;
                        }
                        
                        data.projects.forEach(project => {
                            const projectItem = document.createElement('div');
                            projectItem.className = 'project-item';
                            projectItem.innerHTML = `
                                <div class="project-title">${project.requirement.substring(0, 50)}${project.requirement.length > 50 ? '...' : ''}</div>
                                <div class="project-description">${project.language || 'python'} 项目</div>
                                <div class="project-meta">
                                    <span><i class="far fa-clock"></i> ${project.timestamp}</span>
                                    <span><i class="far fa-file"></i> ${project.files ? project.files.length : 0} 个文件</span>
                                </div>
                            `;
                            projectItem.onclick = () => loadProject(project.project_id);
                            projectsList.appendChild(projectItem);
                        });
                    }
                })
                .catch(error => {
                    console.error('加载项目失败:', error);
                });
        }
        
        function loadProject(projectId) {
            fetch(`/project/${projectId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        currentProjectId = projectId;
                        showResultsPanel();
                        
                        // 显示文件列表
                        const fileList = document.getElementById('fileList');
                        fileList.innerHTML = '';
                        
                        data.files.forEach((file, index) => {
                            const fileItem = document.createElement('div');
                            fileItem.className = 'file-item' + (index === 0 ? ' active' : '');
                            fileItem.textContent = file.name;
                            fileItem.onclick = () => showFileContent(file);
                            fileList.appendChild(fileItem);
                        });
                        
                        // 显示第一个文件的内容
                        if (data.files.length > 0) {
                            showFileContent(data.files[0]);
                        }
                        
                        // 启用下载按钮
                        document.getElementById('downloadBtn').onclick = () => {
                            window.location.href = `/download/${projectId}`;
                        };
                        
                        // 显示成功消息
                        showMessage('项目加载成功！', 'success');
                    }
                })
                .catch(error => {
                    showMessage('加载项目失败: ' + error, 'error');
                });
        }
        
        function showFileContent(file) {
            // 更新激活的文件项
            document.querySelectorAll('.file-item').forEach(item => {
                item.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // 根据文件类型显示内容
            if (file.name.endsWith('.py') || file.name.endsWith('.js') || 
                file.name.endsWith('.java') || file.name.endsWith('.cpp') || 
                file.name.endsWith('.html')) {
                document.getElementById('codeDisplay').textContent = file.content;
                switchTab('codeTab');
            } else if (file.name.includes('review')) {
                document.getElementById('reviewDisplay').innerHTML = `<div class="review-section">${formatText(file.content)}</div>`;
                switchTab('reviewTab');
            } else if (file.name.includes('explanation')) {
                document.getElementById('explanationDisplay').innerHTML = `<div class="code-display">${formatText(file.content)}</div>`;
                switchTab('explanationTab');
            }
        }
        
        function formatText(text) {
            return text.replace(/\n/g, '<br>')
                       .replace(/##(.*?)##/g, '<strong>$1</strong>');
        }
        
        function switchTab(tabName) {
            // 隐藏所有标签内容
            document.querySelectorAll('.tab-content').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // 移除所有标签的激活状态
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // 显示选中的标签内容
            document.getElementById(tabName).classList.add('active');
            
            // 激活对应的标签按钮
            event.target.classList.add('active');
        }
        
        function showResultsPanel() {
            document.getElementById('resultsPanel').style.display = 'block';
        }
        
        function showMessage(message, type) {
            const errorDiv = document.getElementById('errorMessage');
            const successDiv = document.getElementById('successMessage');
            
            if (type === 'error') {
                errorDiv.textContent = message;
                errorDiv.style.display = 'block';
                successDiv.style.display = 'none';
            } else {
                successDiv.textContent = message;
                successDiv.style.display = 'block';
                errorDiv.style.display = 'none';
            }
            
            // 3秒后自动隐藏
            setTimeout(() => {
                errorDiv.style.display = 'none';
                successDiv.style.display = 'none';
            }, 3000);
        }
        
        // 生成代码
        document.getElementById('generateBtn').onclick = function() {
            const requirement = document.getElementById('requirement').value.trim();
            const language = document.getElementById('language').value;
            
            if (!requirement) {
                showMessage('请输入代码需求', 'error');
                return;
            }
            
            // 显示加载中
            document.getElementById('loading').style.display = 'block';
            this.disabled = true;
            
            // 发送请求
            fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    requirement: requirement,
                    language: language
                })
            })
            .then(response => response.json())
            .then(data => {
                // 隐藏加载中
                document.getElementById('loading').style.display = 'none';
                document.getElementById('generateBtn').disabled = false;
                
                if (data.success) {
                    currentProjectId = data.project_id;
                    
                    // 显示结果面板
                    showResultsPanel();
                    
                    // 显示文件列表
                    const fileList = document.getElementById('fileList');
                    fileList.innerHTML = '';
                    
                    if (data.files && data.files.length > 0) {
                        data.files.forEach((file, index) => {
                            const fileName = file.split('/').pop();
                            const fileItem = document.createElement('div');
                            fileItem.className = 'file-item' + (index === 0 ? ' active' : '');
                            fileItem.textContent = fileName;
                            fileItem.onclick = () => {
                                // 模拟显示文件内容
                                if (fileName.includes('.py')) {
                                    document.getElementById('codeDisplay').textContent = data.generation.code;
                                    switchTab('codeTab');
                                }
                            };
                            fileList.appendChild(fileItem);
                        });
                    }
                    
                    // 显示生成的代码
                    if (data.generation && data.generation.code) {
                        document.getElementById('codeDisplay').textContent = data.generation.code;
                        switchTab('codeTab');
                    }
                    
                    // 显示审查结果
                    if (data.review && data.review.review) {
                        const review = data.review.review;
                        let reviewHTML = '<div class="review-section">';
                        
                        if (review.quality_score) {
                            reviewHTML += `<div class="score-badge">质量评分: ${review.quality_score}/10</div>`;
                        }
                        
                        if (review.main_issues) {
                            reviewHTML += '<h3>主要问题</h3><ul class="issues-list">';
                            review.main_issues.split('\n').forEach(issue => {
                                if (issue.trim()) reviewHTML += `<li>${issue}</li>`;
                            });
                            reviewHTML += '</ul>';
                        }
                        
                        if (review.suggestions) {
                            reviewHTML += '<h3>改进建议</h3><ul class="suggestions-list">';
                            review.suggestions.split('\n').forEach(suggestion => {
                                if (suggestion.trim()) reviewHTML += `<li>${suggestion}</li>`;
                            });
                            reviewHTML += '</ul>';
                        }
                        
                        reviewHTML += '</div>';
                        document.getElementById('reviewDisplay').innerHTML = reviewHTML;
                    }
                    
                    // 显示解释
                    if (data.generation && data.generation.explanation) {
                        document.getElementById('explanationDisplay').innerHTML = 
                            `<div class="code-display">${formatText(data.generation.explanation)}</div>`;
                    }
                    
                    // 配置下载按钮
                    document.getElementById('downloadBtn').onclick = () => {
                        window.location.href = `/download/${currentProjectId}`;
                    };
                    
                    showMessage('代码生成成功！', 'success');
                    
                    // 重新加载项目列表
                    loadProjects();
                } else {
                    showMessage('生成失败: ' + (data.error || '未知错误'), 'error');
                }
            })
            .catch(error => {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('generateBtn').disabled = false;
                showMessage('请求失败: ' + error, 'error');
            });
        };
        
        // 新建项目按钮
        document.getElementById('newProjectBtn').onclick = function() {
            document.getElementById('requirement').value = '';
            document.getElementById('resultsPanel').style.display = 'none';
            showMessage('已清空，可以开始新项目', 'success');
        };
        
        // 按Enter键生成代码
        document.getElementById('requirement').addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                document.getElementById('generateBtn').click();
            }
        });
    </script>
</body>
</html>
'''

# 如果没有templates目录，创建并保存HTML
if not os.path.exists('templates'):
    os.makedirs('templates')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_TEMPLATE)

if __name__ == '__main__':
    print("🚀 启动 Code Agent Web 应用...")
    print("🌐 访问地址: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
```

运行Web应用：
```bash
python web_app.py
```

然后打开浏览器访问：`http://localhost:5000`

---

## **第7步：添加高级功能**

创建 `enhancements.py`：
```python
"""
高级功能扩展模块
"""
import subprocess
import sys
import json
from typing import Dict, List

class AdvancedFeatures:
    """Code Agent 的高级功能"""
    
    @staticmethod
    def install_dependencies(code: str) -> List[str]:
        """自动检测并安装Python依赖"""
        imports = []
        
        # 常见的导入映射到包名
        import_map = {
            'flask': 'flask',
            'requests': 'requests',
            'numpy': 'numpy',
            'pandas': 'pandas',
            'matplotlib': 'matplotlib',
            'tensorflow': 'tensorflow',
            'torch': 'torch',
            'django': 'django',
            'sqlalchemy': 'sqlalchemy',
            'beautifulsoup4': 'beautifulsoup4',
            'selenium': 'selenium',
            'pytest': 'pytest',
            'sklearn': 'scikit-learn',
            'cv2': 'opencv-python'
        }
        
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            
            # 检查import语句
            if line.startswith('import ') or line.startswith('from '):
                for lib, package in import_map.items():
                    if lib in line:
                        imports.append(package)
                        break
        
        # 去重
        imports = list(set(imports))
        
        # 安装依赖
        installed = []
        for package in imports:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                installed.append(package)
                print(f"✅ 已安装: {package}")
            except subprocess.CalledProcessError:
                print(f"❌ 安装失败: {package}")
        
        return installed
    
    @staticmethod
    def run_code_tests(code: str, test_code: str = None) -> Dict:
        """运行代码测试"""
        import tempfile
        import os
        
        results = {
            "success": False,
            "output": "",
            "error": "",
            "tests_passed": 0,
            "tests_failed": 0
        }
        
        try:
            # 创建临时文件
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name
            
            if test_code:
                # 如果有测试代码，一起运行
                with tempfile.NamedTemporaryFile(mode='w', suffix='_test.py', delete=False) as f:
                    f.write(test_code)
                    test_file = f.name
                
                try:
                    # 运行测试
                    result = subprocess.run(
                        [sys.executable, '-m', 'pytest', test_file, '-v'],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    results["output"] = result.stdout
                    results["error"] = result.stderr
                    
                    # 解析测试结果
                    if "passed" in result.stdout:
                        passed = result.stdout.count("PASSED")
                        failed = result.stdout.count("FAILED")
                        results["tests_passed"] = passed
                        results["tests_failed"] = failed
                        results["success"] = failed == 0
                
                finally:
                    os.unlink(test_file)
            else:
                # 直接运行代码
                result = subprocess.run(
                    [sys.executable, temp_file],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                results["output"] = result.stdout
                results["error"] = result.stderr
                results["success"] = result.returncode == 0
            
        except subprocess.TimeoutExpired:
            results["error"] = "执行超时"
        except Exception as e:
            results["error"] = str(e)
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
        
        return results
    
    @staticmethod
    def generate_documentation(code: str) -> str:
        """生成代码文档"""
        # 这是一个简化的示例，实际可以使用更复杂的文档生成工具
        lines = code.split('\n')
        
        doc_lines = ["# 代码文档", ""]
        
        current_func = None
        for i, line in enumerate(lines):
            line = line.strip()
            
            # 检测函数定义
            if line.startswith('def '):
                func_name = line.split('def ')[1].split('(')[0]
                doc_lines.append(f"## 函数: {func_name}")
                doc_lines.append(f"**定义**: `{line}`")
                current_func = func_name
            
            # 检测类定义
            elif line.startswith('class '):
                class_name = line.split('class ')[1].split('(')[0].split(':')[0]
                doc_lines.append(f"## 类: {class_name}")
                doc_lines.append(f"**定义**: `{line}`")
                current_func = None
            
            # 检测注释
            elif line.startswith('#'):
                if current_func:
                    doc_lines.append(f"**说明**: {line[1:].strip()}")
                else:
                    doc_lines.append(f"- {line[1:].strip()}")
        
        return '\n'.join(doc_lines)
    
    @staticmethod
    def optimize_code(code: str) -> Dict:
        """代码优化建议"""
        suggestions = []
        
        # 检查重复代码
        lines = code.split('\n')
        line_counts = {}
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                line_counts[stripped] = line_counts.get(stripped, 0) + 1
        
        for line, count in line_counts.items():
            if count > 3 and len(line) > 20:  # 重复的较长行
                suggestions.append(f"可能的重复代码: '{line[:50]}...' 出现了 {count} 次")
        
        # 检查长函数
        func_lines = 0
        in_func = False
        for line in lines:
            if line.strip().startswith('def '):
                if in_func and func_lines > 50:
                    suggestions.append(f"函数过长: {func_lines} 行，建议拆分为小函数")
                in_func = True
                func_lines = 0
            elif in_func:
                if line.strip() and not line.strip().startswith('#'):
                    func_lines += 1
                if line.strip() == '' and lines[lines.index(line)-1].strip().endswith(':'):
                    in_func = False
        
        return {
            "suggestions": suggestions,
            "score": max(0, 10 - len(suggestions))  # 简单的评分
        }


# 测试高级功能
def test_advanced_features():
    """测试高级功能"""
    print("🧪 测试高级功能...")
    
    # 测试代码
    test_code = """
import requests
import numpy as np
from flask import Flask

app = Flask(__name__)

def long_function():
    # 这是一个很长的函数
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    # 重复的行
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t

@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run()
"""
    
    print("1. 生成文档:")
    doc = AdvancedFeatures.generate_documentation(test_code)
    print(doc[:500] + "..." if len(doc) > 500 else doc)
    
    print("\n2. 优化建议:")
    optim = AdvancedFeatures.optimize_code(test_code)
    for suggestion in optim["suggestions"]:
        print(f"  - {suggestion}")
    print(f"优化评分: {optim['score']}/10")
    
    print("\n3. 检测依赖:")
    imports = AdvancedFeatures.install_dependencies(test_code)
    print(f"检测到的依赖: {imports}")
    
    # 注意：运行测试功能需要谨慎，因为它会实际执行代码
    # print("\n4. 运行测试:")
    # test_result = AdvancedFeatures.run_code_tests(test_code)
    # print(f"执行成功: {test_result['success']}")
    # if test_result['error']:
    #     print(f"错误: {test_result['error']}")


if __name__ == "__main__":
    test_advanced_features()
```

---

## **第8步：创建完整的项目结构**

现在整理所有文件，创建完整的项目结构：

```
code-agent-tutorial/
│
├── .env                    # 环境变量（API密钥）
├── .gitignore             # Git忽略文件
├── requirements.txt       # Python依赖
│
├── api_client.py          # API客户端模块
├── code_generator.py      # 代码生成器
├── code_reviewer.py       # 代码审查器
├── code_agent.py          # 主Agent类
├── enhancements.py        # 高级功能
├── web_app.py             # Web应用
│
├── templates/             # HTML模板
│   └── index.html
│
├── workspace/             # 生成的项目文件
│   └── (自动生成的项目)
│
└── README.md              # 项目说明
```

创建 `README.md`：
```markdown
# 🤖 Code Agent - AI编程助手

一个基于DeepSeek API的智能代码生成与审查系统。

## ✨ 功能特性

- ✅ AI代码生成：根据自然语言描述生成代码
- ✅ 智能代码审查：分析代码质量、安全性、性能
- ✅ 项目自动管理：保存历史项目，支持下载
- ✅ Web界面：友好的图形用户界面
- ✅ 多语言支持：Python、JavaScript、Java、C++等
- ✅ 复杂度分析：自动评估代码复杂度

## 🚀 快速开始

### 1. 环境准备
```bash
# 克隆项目
git clone <项目地址>
cd code-agent-tutorial

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置API密钥
1. 访问 [DeepSeek平台](https://platform.deepseek.com/)
2. 获取API密钥
3. 在项目根目录创建 `.env` 文件：
```
DEEPSEEK_API_KEY=你的API密钥
```

### 3. 运行应用
```bash
# 启动Web应用
python web_app.py

# 访问 http://localhost:5000
```

## 📁 项目结构

```
code-agent-tutorial/
├── api_client.py      # API客户端
├── code_generator.py  # 代码生成模块
├── code_reviewer.py   # 代码审查模块
├── code_agent.py      # 主Agent类
├── web_app.py         # Web应用
└── workspace/         # 生成的项目文件
```

## 🛠️ 使用方法

### 基础使用
1. 打开Web界面 (`http://localhost:5000`)
2. 在文本框中输入代码需求
3. 选择编程语言
4. 点击"生成代码"
5. 查看生成的代码、审查报告和解释

### 命令行使用
```bash
# 直接测试代码生成
python code_generator.py

# 测试代码审查
python code_reviewer.py

# 测试完整流程
python code_agent.py
```

## 🔧 高级功能

### 1. 添加自定义模板
修改 `code_generator.py` 中的 `system_prompt` 来自定义生成风格。

### 2. 扩展语言支持
在 `LANGUAGE_TEMPLATES` 中添加新的编程语言配置。

### 3. 集成版本控制
可以添加Git集成，自动提交生成的代码。

## 📊 成本估算

- 小型项目：约 $0.01 - $0.05
- 中型项目：约 $0.05 - $0.20
- 大型项目：约 $0.20 - $0.50

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 📄 许可证

MIT License

## 🙏 致谢

- 感谢 DeepSeek 提供强大的AI API
- 感谢所有开源项目的贡献者

## 📞 支持

遇到问题？请：
1. 检查API密钥是否正确
2. 确保网络连接正常
3. 查看控制台错误信息
4. 提交Issue到GitHub
```

---

## **第9步：部署上线**

### **9.1 本地生产部署**
创建 `run_production.py`：
```python
from web_app import app

if __name__ == '__main__':
    # 生产环境配置
    app.config.update(
        DEBUG=False,
        SECRET_KEY='your-secret-key-here-change-this'
    )
    
    print("🚀 启动生产服务器...")
    print("🌐 访问地址: http://localhost:5000")
    print("📁 工作空间: ./workspace")
    print("⚠️  按 Ctrl+C 停止服务器")
    
    app.run(host='0.0.0.0', port=5000)
```

### **9.2 Docker部署**
创建 `Dockerfile`：
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 创建工作空间目录
RUN mkdir -p workspace

# 设置环境变量
ENV FLASK_APP=web_app.py
ENV FLASK_ENV=production

# 暴露端口
EXPOSE 5000

# 运行应用
CMD ["python", "web_app.py"]
```

创建 `docker-compose.yml`：
```yaml
version: '3.8'

services:
  code-agent:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./workspace:/app/workspace
      - ./.env:/app/.env
    environment:
      - DEEPSEEK_API_KEY=${DEEPSEEK_API_KEY}
    restart: unless-stopped
```

### **9.3 云部署指南**

#### **部署到 Railway**
```bash
# 1. 安装Railway CLI
npm i -g @railway/cli

# 2. 登录
railway login

# 3. 初始化项目
railway init

# 4. 部署
railway up
```

#### **部署到 Render**
1. 创建 `render.yaml`：
```yaml
services:
  - type: web
    name: code-agent
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python web_app.py
    envVars:
      - key: DEEPSEEK_API_KEY
        sync: false
```

#### **部署到 PythonAnywhere**
1. 上传所有文件到PythonAnywhere
2. 在Web应用配置中设置虚拟环境
3. 配置WSGI文件
4. 设置环境变量

---

## **🎉 恭喜！你已经完成了Code Agent的开发！**

### **下一步学习方向：**

1. **性能优化**
   - 添加缓存机制
   - 实现流式响应
   - 优化API调用频率

2. **功能扩展**
   - 添加代码调试功能
   - 支持更多编程语言
   - 集成Git版本控制
   - 添加代码格式化

3. **用户体验**
   - 添加代码编辑器（CodeMirror/Monaco）
   - 实现实时预览
   - 添加用户账户系统

4. **部署优化**
   - 添加数据库支持
   - 实现负载均衡
   - 添加监控和日志

### **实用命令总结：**

```bash
# 开发环境
python web_app.py                    # 启动开发服务器

# 生产环境
python run_production.py             # 启动生产服务器

# Docker
docker build -t code-agent .         # 构建镜像
docker run -p 5000:5000 code-agent   # 运行容器

# 维护
python code_agent.py                 # 命令行模式
python enhancements.py               # 测试高级功能
```

### **遇到问题怎么办？**

1. **API调用失败**
   - 检查API密钥是否正确
   - 确认网络连接
   - 查看DeepSeek API状态

2. **代码生成质量不高**
   - 优化系统提示词
   - 调整温度参数
   - 提供更详细的描述

3. **Web界面无法访问**
   - 检查端口是否被占用
   - 查看Flask日志
   - 确认依赖安装正确

---

**现在你已经有了一个完整的Code Agent！** 你可以：

1. 继续添加新功能
2. 优化现有代码
3. 部署到云服务器
4. 分享给朋友使用

有什么具体问题或者想继续扩展哪个功能吗？我很乐意继续帮助你！ 😊