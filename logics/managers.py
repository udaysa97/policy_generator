from statistics import mode
import os
from logics.models import Employee, Policies, AcceptedPolicies
from datetime import datetime, timedelta


class PoliciyManager():
    def __init__(self, emp_id, role):
        self.emp_id = emp_id
        self.role = role

    def get_pending_policies(self):
        
        emp_policies = Policies.objects.filter(applicable_to__icontains=self.role, is_approved=True, is_latest=True)
        accepted_policies = AcceptedPolicies.objects.filter(fk_employee__emp_id=self.emp_id)

        new_user = len(accepted_policies) == 0
        is_reaccept = False
        
        pending_policies = []

        for policy in emp_policies:
            policy_found = False
            for acc_policies in accepted_policies:
                if (acc_policies.fk_policy.id == policy.id and ((new_user and acc_policies.last_updated_on + \
                     timedelta(days=30) > datetime.now()) or\
                          (not new_user and acc_policies.last_updated_on + timedelta(days=int(os.environ['POLICYRENEW'])) > datetime.now()))):
                    if(acc_policies['need_re_accept']):
                        break # need to add logic here to change object to send this att to be saved in DB later wehn accepting
                    policy_found = True
                    break
                # else code for time calculation and sending mail in case time period exceeds 30 days of notice
            
            if not policy_found:
                pending_policies.append(policy)

        return {'pending_policies': pending_policies , 'new_user': new_user}

class PolicyAcceptManager():

    def accept_policies(self, policy_emp_list):

        for data in policy_emp_list:
            emp_id = data['emp_id']
            policy_id = data['policy_id']

            policies = AcceptedPolicies.objects.filter(fk_employee__emp_id=emp_id, fk_policy__policy_id=policy_id).order_by('-last_updated_on')
            if(len(policies) > 0):
                policyToUpdate = policies.first()
                policyToUpdate.need_re_accept = True
                policyToUpdate.save()
            else:
                AcceptedPolicies.objects.create(
                fk_employee = Employee.objects.get(emp_id=emp_id),
                is_periodic = False,
                is_reAccept = True,
                need_re_accept = True,
                fk_policy = policies.first()
            )






