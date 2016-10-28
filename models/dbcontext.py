from models.teamrole import *
from models.portfolio import *
from models.users import *
from models.mlab import *

def add_team_roles():
    for team_role in TeamRole.objects:
        team_role.delete()
    (TeamRole(title="Product Manager",code="PO")).save()
    (TeamRole(title="Scrum Master",code="SM")).save()
    (TeamRole(title="Team member",code="Team member")).save()

def add_porfolios():
    for p in Portfolio.objects:
        p.delete()
    Portfolio(title="Keep healthy",image="http://techkids.vn:9196/img_hackathon/team6/d6.png",description="KEEP HEALTHY là sản phẩm dành cho những người làm việc chủ yếu trong văn phòng, phải ngồi lâu một chỗ, ít có thời gian tập thể dục,… Ứng dụng gồm các bài tập thở giúp rèn luyện sức khỏe, thư giãn tinh thần, luyện tập thở theo phương pháp yoga để có sức khỏe tốt nhất. Hy vọng rằng Keep Healthy sẽ là người bạn đồng hành cùng sức khỏe của bạn.").save()
    Portfolio(title="Pick one",image="http://techkids.vn:9196/img_hackathon/team4/d4.png",description="PICK_ONE là một ứng dụng giúp tìm kiếm thông tin các cửa hàng sửa chữa xe cộ, máy tính, điện thoại, đồ gia dụng gần nhất, nhanh nhất và chi tiết nhất theo yêu cầu, Mọi thông tin cửa hàng bao gồm dịch vụ, giới thiệu bằng lời, ảnh chụp, địa chỉ chính xác trên Google Maps, hướng dẫn đường đi từ địa chỉ hiện tại của bạn đến cửa hàng.").save()

def add_users():
    for user in User.objects:
        user.delete()
    (User(username="admin", password="codethechangevn@2015")).save()

if __name__ == "__main__":
    mlab_connect()
    ##add_team_roles()
    ##add_porfolios()
    ##add_users()
    mlab_disconnect()