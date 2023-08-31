using CR_API.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace CR_API.Controllers
{
    public class UsersTicketController : ApiController
    {
        [Route("api/usersticket/getall")]
        [HttpGet]
        public IEnumerable<Users> GetAll()
        {
            using (QAOrgEntities dbContext = new QAOrgEntities())
            {
                return dbContext.Users.ToList();
            }
        }
    }
}
